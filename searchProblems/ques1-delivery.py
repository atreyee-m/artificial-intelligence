#Description: This problem deals with 5 people, 5 packages that was to be delivered to them and their respective locations. So we've taken all possibe combinations of the customer names, items and the location. We've kept track of both ordered and received items. We had a huge search space in this way. In order to reduce the space complexity of the problem, we've applied the clues given in the question to reduce the search space. The way that we did it, has been mentioned as comments in the code.
#We formulated a list of posssibilities for each of the customers and then searched by a brute force method.
#The clues weren't easy to derive. Hence reduction of the search space was difficult.
#Output of the problem:
#Solution
#-----------------------------------------------------------
#George received Candelabrum ordered Banister lives in Lake Avenue
#Irene received Banister ordered Candelabrum lives in Kirkwood Street
#Heather received Elephant ordered Amplifier lives in North Avenue
#Jerry received Amplifier ordered Doorknob lives in Maxwell Street
#Frank received Doorknob ordered Elephant lives in Orange Drive



__author__ = 'atreyee'
import itertools

# Exhaustive Search#

customers=['George', 'Heather', 'Jerry', 'Irene', 'Frank']
items=['Banister', 'Candelabrum', 'Elephant', 'Amplifier', 'Doorknob']
streets=['Kirkwood Street', 'Maxwell Street', 'Orange Drive', 'North Avenue', 'Lake Avenue']
def is_duplictate(configuration, next_config):
    customer_list=[]
    received_items=[]
    ordered_items=[]
    street_list=[]

    for config in configuration:
        customer_list.append(config['customer'])
        received_items.append(config['received'])
        ordered_items.append(config['ordered'])
        street_list.append(config['street'])

    if next_config['customer'] in customer_list:
        return True

    if next_config['received'] in received_items:

        return True

    if next_config['ordered'] in ordered_items:
      #  print ordered_items
       # print next_config['ordered'] + " is duplicate"
        return True

    if next_config['street'] in street_list:
       # print street_list
       # print next_config['street'] + "is duplicate"
        return True
    return False


def is_it_a_solution(possible_solution):
    irenes_config=[]
    georges_config=[]
    lake_av=[]
    orange_dr=[]
    jerrys_config=[]
    maxwell_st=[]
    config_list=[]

    for finding_config in possible_solution:
        if finding_config['customer']=='Irene':
            irenes_config=finding_config
        if finding_config['customer']=='Jerry':
            jerrys_config=finding_config
        if finding_config['customer']=='George':
            georges_config=finding_config
        if finding_config['street']=='Lake Avenue':
            lake_av=finding_config
        if finding_config['street']=='Orange Drive':
            orange_dr=finding_config
        if finding_config['street']=='Maxwell Street':
            maxwell_st=finding_config

    for config in possible_solution:
        if config['ordered']=='Banister':
            if config['received']!=irenes_config['ordered']:
                return False
        if config['street']=='Kirkwood Street':
            if config['received']!=georges_config['ordered']:
                return False
            if config['ordered']!=lake_av['received']:
                return False
        if config['customer']=='Heather':
            if config['received']!=orange_dr['ordered']:
                return False
            if jerrys_config['received']!=config['ordered']:
                return False
        if config['ordered']=='Elephant':
            if config['received']!=maxwell_st['ordered']:
                return False





    return True
def main():
    detail_info=list()
    georges_detail=list()
    irenes_detail=list()
    heathers_detail=list()
    jerrys_detail=list()
    franks_detail=list()


    paired_items=list(itertools.permutations(items, 2))
    paired_customers=list(itertools.permutations(customers,5))

    for customer in customers:
        #row={}
        for street in streets:
            for pair in paired_items:


                # 1. The customer who ordered the Cabdelabrum received the Banister, which means if order is candelabrum them received must be Banister
                if (pair[0]=='Candelabrum' and pair[1]!='Banister') or (pair[1]=='Banister' and pair[0]!='Candelabrum'):
                    continue

                 # 2. The person who ordered Banister received Irenes Packge; Which means Irene did not order Banister
                elif customer=='Irene' and pair[0]=='Banister':
                    continue
                # 3. Frank Received a Doorknob
                elif customer=='Frank' and pair[1]!='Doorknob':
                    continue

                    # 3. Frank Received a Doorknob
                elif customer=='Frank' and pair[0]=='Candelabrum':
                    continue

                elif customer=='Frank' and pair[0]=='Banister':
                    continue

                # 4. George's package went to Kirkwood Street, which implies that George does not live in Kirkwood street
                elif customer=='George' and street=='Kirkwood Street':
                    continue

                # 6. Heather received the package that was to go to Orange Drive, which implies that Heather does not live in Orange Drive
                elif customer=='Heather' and street=='Orange Drive':
                    continue

                elif customer=='Heather' and pair[0]=='Doorknob':
                    continue
                # 8. The Elephant arrived in North Avenue
                elif (pair[1]!='Elephant' and street=='North Avenue') or (pair[1]=='Elephant' and street!='North Avenue'):
                    continue
                elif (pair[0]=='Elephant' and street=='Kirkwood Street'):
                    continue

                 # 9. The Elephant arrived in North Avenue; the person who had ordered it received the package that should have gone to Maxwell Street. Elephant did not ordered from Maxwell Street
                elif (pair[0]=='Elephant' and street=='Maxwell Street') :
                    continue

                # 10. Maxwell Street received the Amplifier
                elif (pair[1]!='Amplifier' and street=='Maxwell Street') or (pair[1]=='Amplifier' and street!='Maxwell Street'):
                    continue



                else:
                    row={}
                    row['customer']=customer
                    row['ordered']=pair[0]
                    row['received']=pair[1]
                    row['street']=street
                    detail_info.append(row)
                    if customer=='George':
                        georges_detail.append(row)
                    if customer=='Frank':
                        franks_detail.append(row)
                    if customer=='Irene':
                        irenes_detail.append(row)
                    if customer=='Heather':
                        heathers_detail.append(row)
                    if customer=='Jerry':
                        jerrys_detail.append(row)



    found_solution=[]
    for c in paired_customers:


        name_1=c[0].lower()+'s_detail'
        name_2=c[1].lower()+'s_detail'
        name_3=c[2].lower()+'s_detail'
        name_4= c[3].lower()+'s_detail'
        name_5=c[4].lower()+'s_detail'

        detail_1=eval(name_1)
        detail_2=eval(name_2)
        detail_3=eval(name_3)
        detail_4=eval(name_4)
        detail_5=eval(name_5)

        for details1 in detail_1:
            possible_solution=[]
            possible_solution.append(details1)
            for details2 in detail_2:
                if routine_check(possible_solution, details2):
                    for details3 in detail_3:
                        if routine_check(possible_solution, details3):
                            for details4 in detail_4:
                                if routine_check(possible_solution, details4):
                                    for details5 in detail_5:
                                        if routine_check(possible_solution, details5):
                                            if is_it_a_solution(possible_solution):
                                                Solution(possible_solution)
                                                return




def Solution(possible_solution):
    print "Possible Solution"
    print '-----------------------------------------------------------'
    for config in possible_solution:
        print config['customer'] +' received '+config['received'] +' ordered '+config['ordered']+' lives in '+ config['street']

def routine_check(possible_solution,detail):

    if is_duplictate(possible_solution,detail):
        return False
    else:
        possible_solution.append(detail)
      #  print possible_solution
        return True
    return False
if __name__ == "__main__":
    main()
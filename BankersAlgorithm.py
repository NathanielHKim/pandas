#Nathaniel Kim
#G01197966

#first make a list called claim_vec that represents the Claim Vector shown in the instructions
claim_vec = [8, 5, 9, 7]

#then establish the allocated resource table as mutiple lists, with allo_px representing each list
allo_p0 = [2, 0, 1, 1]
allo_p1 = [0, 1, 2, 1]
allo_p2 = [4, 0, 0, 3]
allo_p3 = [0, 2, 1, 0]
allo_p4 = [1, 0, 3, 0]

#Now establish the maximum claim table as mutiple lists as well instead of a matrix individually
max_claim_p0 = [3, 2, 1, 4]
max_claim_p1 = [0, 2, 5, 2]
max_claim_p2 = [5, 1, 0, 5]
max_claim_p3 = [1, 5, 3, 0]
max_claim_p4 = [3, 0, 3, 3]

#now we begin banker's alogorithm
#the new groups of lists named need_px represents the need matrix which is represented by the formula Max - Allocation = Need
need_p0 = [max_claim_p0[0] - allo_p0[0], max_claim_p0[1] - allo_p0[1], max_claim_p0[2] - allo_p0[2], max_claim_p0[3] - allo_p0[3]]
need_p1 = [max_claim_p1[0] - allo_p1[0], max_claim_p1[1] - allo_p1[1], max_claim_p1[2] - allo_p1[2], max_claim_p1[3] - allo_p1[3]]
need_p2 = [max_claim_p2[0] - allo_p2[0], max_claim_p2[1] - allo_p2[1], max_claim_p2[2] - allo_p2[2], max_claim_p2[3] - allo_p2[3]]
need_p3 = [max_claim_p3[0] - allo_p3[0], max_claim_p3[1] - allo_p3[1], max_claim_p3[2] - allo_p3[2], max_claim_p3[3] - allo_p3[3]]
need_p4 = [max_claim_p4[0] - allo_p4[0], max_claim_p4[1] - allo_p4[1], max_claim_p4[2] - allo_p4[2], max_claim_p4[3] - allo_p4[3]]

#now we have each need value for each process




#the variable i is used to represent the index of each list that is used
i = 0

#this is the next step of Banker's algorithm
#the first if and elif statement is used to test the available, checking if each and every claim vector value is greater than the P0 need values individually
#if it is greater, P0 is established at True, and if not, P0 is established as False and the print statement: 'system is not safe' is printed
#in both scenarios, the NEW availability is created, and named new_avail_1, as a new list to be used as the NEW claim vector for the P1 or next need value.
if ((claim_vec[i] >= need_p0[i]) & (claim_vec[i+1] >= need_p0[i+1]) & (claim_vec[i+2] >= need_p0[i+2]) & (claim_vec[i+3] >= need_p0[i+3])):
    #as a result of the if statement, the process below follows through with the formula: Available+Allocation = New Available, to find the list that makes each sequence safe or TRUE
    new_avail_1 = [claim_vec[i] + allo_p0[i], claim_vec[i+1] + allo_p0[i+1], claim_vec[i+2] + allo_p0[i+2], claim_vec[i+3] + allo_p0[i+3]]
    p0 = True
elif ((claim_vec[i] < need_p0[i]) | (claim_vec[i+1] < need_p0[i+1]) | (claim_vec[i+2] < need_p0[i+2]) | (claim_vec[i+3] < need_p0[i+3])):
    new_avail_1 = claim_vec
    p0 = False
    print('System is not safe!')
    

#the second if and elif statement is used to test the available, checking if each and every claim vector(named new_avail_1) value is greater than the P1 need values individually
#if it is greater, P1 is established at True, and if not, P1 is established as False and the print statement: 'system is not safe' is printed
#in both scenarios, the NEW availability is created, and named new_avail_2, as a new list to be used as the NEW claim vector for the P2 or next need value.        
if ((new_avail_1[i] >= need_p1[i]) & (new_avail_1[i+1] >= need_p1[i+1]) & (new_avail_1[i+2] >= need_p1[i+2]) & (new_avail_1[i+3] >= need_p1[i+3])):
        #as a result of the if statement, the process below follows through with the formula: Available+Allocation = New Available, to find the list that makes each sequence safe or TRUE
      new_avail_2 = [new_avail_1[i] + allo_p1[i], new_avail_1[i+1] + allo_p1[i+1], new_avail_1[i+2] + allo_p1[i+2], new_avail_1[i+3] + allo_p1[i+3]]
      p1 = True
       

elif ((new_avail_1[i] < need_p1[i]) | (new_avail_1[i+1] < need_p1[i+1]) | (new_avail_1[i+2] < need_p1[i+2]) | (new_avail_1[i+3] < need_p1[i+3])):
       new_avail_2 = new_avail_1
       p1 = False
       print('System is not safe!')


#the third if and elif statement is used to test the available, checking if each and every claim vector(named new_avail_2) value is greater than the P2 need values individually
#if it is greater, P2 is established at True, and if not, P2 is established as False and the print statement: 'system is not safe' is printed
#in both scenarios, the NEW availability is created, and named new_avail_3, as a new list to be used as the NEW claim vector for the P3 or next need value. 
if ((new_avail_2[i] >= need_p2[i]) & (new_avail_2[i+1] >= need_p2[i+1]) & (new_avail_2[i+2] >= need_p2[i+2]) & (new_avail_2[i+3] >= need_p2[i+3])):
        #as a result of the if statement, the process below follows through with the formula: Available+Allocation = New Available, to find the list that makes each sequence safe or TRUE
       new_avail_3 = [new_avail_2[i] + allo_p2[i], new_avail_2[i+1] + allo_p2[i+1], new_avail_2[i+2] + allo_p2[i+2], new_avail_2[i+3] + allo_p2[i+3]]
       p2 = True

elif ((new_avail_2[i] < need_p2[i]) | (new_avail_2[i+1] < need_p2[i+1]) | (new_avail_2[i+2] < need_p2[i+2]) | (new_avail_2[i+3] < need_p2[i+3])):
       new_avail_3 = new_avail_2
       p2 = False
       print('System is not safe!')


#the fourth if and elif statement is used to test the available, checking if each and every claim vector(named new_avail_3) value is greater than the P3 need values individually
#if it is greater, P3 is established at True, and if not, P3 is established as False and the print statement: 'system is not safe' is printed
#in both scenarios, the NEW availability is created, and named new_avail_4, as a new list to be used as the NEW claim vector for the P4 or next need value.
if ((new_avail_3[i] >= need_p3[i]) & (new_avail_3[i+1] >= need_p3[i+1]) & (new_avail_3[i+2] >= need_p3[i+2]) & (new_avail_3[i+3] >= need_p3[i+3])):
        #as a result of the if statement, the process below follows through with the formula: Available+Allocation = New Available, to find the list that makes each sequence safe or TRUE
       new_avail_4 = [new_avail_3[i] + allo_p3[i], new_avail_3[i+1] + allo_p3[i+1], new_avail_3[i+2] + allo_p3[i+2], new_avail_3[i+3] + allo_p3[i+3]]
       p3 = True

elif ((new_avail_3[i] < need_p3[i]) | (new_avail_3[i+1] < need_p3[i+1]) | (new_avail_3[i+2] < need_p3[i+2]) | (new_avail_3[i+3] < need_p3[i+3])):
       new_avail_4 = new_avail_3
       p3 = False
       print('System is not safe!')


#the fifth if and elif statement is used to test the available, checking if each and every claim vector(named new_avail_4) value is greater than the P4 need values individually
#if it is greater, P4 is established at True, and if not, P4 is established as False and the print statement: 'system is not safe' is printed
#in both scenarios, the NEW availability is created, and named new_avail_5,there will not be any more claim vectors because there are no more resources available.
if ((new_avail_4[i] >= need_p4[i]) & (new_avail_4[i+1] >= need_p4[i+1]) & (new_avail_4[i+2] >= need_p4[i+2]) & (new_avail_4[i+3] >= need_p4[i+3])):
        #as a result of the if statement, the process below follows through with the formula: Available+Allocation = New Available, to find the list that makes each sequence safe or TRUE
       new_avail_5 = [new_avail_4[i] + allo_p4[i], new_avail_4[i+1] + allo_p4[i+1], new_avail_4[i+2] + allo_p4[i+2], new_avail_4[i+3] + allo_p4[i+3]]
       p4 = True

elif ((new_avail_4[i] < need_p4[i]) | (new_avail_4[i+1] < need_p4[i+1]) | (new_avail_4[i+2] < need_p4[i+2]) | (new_avail_4[i+3] < need_p4[i+3])):
       new_avail_5 = new_avail_4
       p4 = False
       print('System is not safe!')
       
#this final if statement is the final check if the system is in a safe state and will print "system is safe' and the safe sequence as well       
if (p0==True & p1==True & p2==True & p3==True & p4==True):
    print('System is safe!')
    print('Safe sequence is: P0 P1 P2 P3 P4')


#this section prints all of the NEW availability lists or matrix to show all the safe sequence/new available matrix in the form of lists
print(claim_vec)
print(new_avail_1)
print(new_avail_2)
print(new_avail_3)
print(new_avail_4)
print(new_avail_5)



    
 

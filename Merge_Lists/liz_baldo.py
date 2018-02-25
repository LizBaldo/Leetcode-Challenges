"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
Source: https://leetcode.com/problems/merge-two-sorted-lists/#/description
"""

def merge_two_list_helper(list1, list2):

        new_list = []
        for i in range(len(list1)+len(list2)):
                if list1 == []:
                        new_list.extend(list2)
                        return new_list
                elif list2 == []:
                        new_list.extend(list1)
                        return new_list
                if list1[0] < list2[0]:
                        new_list.append(list1.pop(0))
                else:
                        new_list.append(list2.pop(0))
        
        return new_list
                                
                        

#DO NOT CHANGE THIS FUNCTION
def merge_two_list(list1,list2):
	return merge_two_list_helper(list1, list2)


#test cases
def main():
    list1 = [1,3,5]
    list2 = [2,4,6]
    print ("merging [1,3,5] and [2,4,6]......")
    print ("expected result is [1,2,3,4,5,6]")
    print ("your output is {}".format(merge_two_list(list1, list2)))

if __name__ == "__main__":
    main()

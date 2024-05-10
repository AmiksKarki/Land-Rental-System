
def landList():
    landList=[]
    file=open("landList.txt","r")
    for row in file.readlines(): #returns all lines in the file, as a list where each line is an item in the list but the item is stored as a single string for eg: ['101, Kathmandu, North, 4, 50000, Available']
        row=row.replace('\n', '').split(',')#split method converts a string to list; here , is separator and it makes words separated by , as item in a list
        landList.append(row)
    file.close()
    return landList

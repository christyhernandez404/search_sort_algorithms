from flask import Flask, request, jsonify

app = Flask(__name__)



video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

#Implement the binary search algorithm for searching videos by title.
def binary_search(alist, target):
    high = len(alist)
    low = 0

    while low <= high:
        mid = (low + high)//2 #floor division to return an integer if low+high = odd num
        if alist[mid] == target:
            print("Item is found at this index:")
            return mid
        elif alist[mid] < target:
            low = mid + 1
        else:
            high = mid -1


    print("Item not found") #will indicate target was not found in the list  
    return -1 


def bubble_sort(alist):
    z = len(alist)

    for a in range(z):
        for b in range(0,z - a - 1):
            if alist[b] > alist[b+1]:
                alist[b], alist[b+1] = alist[b+1], alist[b]
    return alist

print(bubble_sort(video_titles)) #prints sorted video_titles list

sorted_titles = bubble_sort(video_titles)

#ensure your binary search is searching through a sorted list
print(binary_search(video_titles,"Digital Photography Essentials")) 


#Develop a REST API endpoint using Flask that allows users to search for videos 
# by their titles using the binary search developed 
@app.route('/search', methods=["GET"])
def search():
    title = request.args.get('title')
   
    index = binary_search(sorted_titles, title)
    if index != -1:
        return jsonify({"message": "Title found!", "title": sorted_titles[index]}), 200
    else:
        return jsonify({"message": "Title not found -_-"}), 404

if __name__ == '__main__':
    app.run(debug=True)

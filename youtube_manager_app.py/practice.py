import json

# Load data from file
def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to file
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file, indent=4)

# Show list of videos
def list_of_videos(videos):
    if not videos:
        print(" No videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']} ({video['time']})")

# Add new video
def add_videos(videos):
    name = input(" Enter video name: ")
    time = input(" Enter video duration: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("Video added successfully!")

# Update existing video
def update_videos(videos):
    list_of_videos(videos)
    try:
        index = int(input("Enter video number to update: ")) - 1
        if 0 <= index < len(videos):
            name = input(f"Enter new name ({videos[index]['name']}): ") or videos[index]['name']
            time = input(f"Enter new time ({videos[index]['time']}): ") or videos[index]['time']
            videos[index] = {"name": name, "time": time}
            save_data_helper(videos)
            print(" Video updated successfully!")
        else:
            print(" Invalid video number.")
    except ValueError:
        print(" Please enter a valid number.")

# Delete a video
def delete_videos(videos):
    list_of_videos(videos)
    try:
        index = int(input("Enter video number to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted_video = videos.pop(index)
            save_data_helper(videos)
            print(f" Deleted: {deleted_video['name']}")
        else:
            print(" Invalid video number.")
    except ValueError:
        print(" Please enter a valid number.")

# Main app loop
def main():
    videos = load_data()
    while True:
        print("\n YouTube Video Manager ")
        print("1: List videos")
        print("2: Add a video")
        print("3: Update video details")
        print("4: Delete a video")
        print("5: Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        match choice:
            case 1:
                list_of_videos(videos)
            case 2:
                add_videos(videos)
            case 3:
                update_videos(videos)
            case 4:
                delete_videos(videos)
            case 5:
                print("Exiting YouTube app. Goodbye!")
                break
            case _:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
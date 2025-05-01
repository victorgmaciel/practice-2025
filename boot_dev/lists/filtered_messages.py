# We need to filter the profanity out of our game's live chat feature!
# Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:
#
# A list of the same messages but with all instances of the word dang removed.
# A list containing the number of dang words that were removed from the message at that particular index.

# Input:
#  * messages: ['darn it', "this dang thing won't work", 'lets fight one on one']
# Expecting:
#  * filtered messages: ['darn it', "this thing won't work", 'lets fight one on one']
#  * words removed: [0, 1, 0]
# Actual:
#  * filtered messages: darn it this thing won't work lets fight one on one
#  * words removed: [0, 1, 0]
# Fail

message_one = ['darn it', "this dang thing won't work", 'lets fight one on one']

def filter_messages(messages):
    filtered_messages = []
    dang_count_index = []


    for message in range(len(messages)):
        messages_split = messages[message].split()
        counter = 0
        clean_words = []
        for mess in messages_split:
            if mess == "dang":
                counter += 1

            else:
                clean_words.append(mess)
        filtered_messages.append(" ".join(clean_words))

        dang_count_index.append(counter)
    return filtered_messages, dang_count_index




print(filter_messages(message_one))
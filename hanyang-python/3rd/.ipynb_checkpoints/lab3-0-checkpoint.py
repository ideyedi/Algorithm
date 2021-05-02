# version 3.9.2
#!/bin/python3

class ReplyAdmin:
    reply_list = []

    def getChatCount(self):
        return len(self.reply_list)

    def addChat(self, chat):
        self.reply_list.append(chat)
        return

    def removeChat(self, idx):
        new_replys = self.reply_list[:idx] + self.reply_list[(idx+1):]
        self.reply_list = new_replys
        return

    def removeChatRange(self, start, end):
        # using slicing
        new_replys = self.reply_list[:start] + self.reply_list[(end+1):]
        self.reply_list = new_replys
        return 

    def removeChatList(self, idx_list):
        new_replys = []
        count = self.getChatCount()
        for idx in range(0, count):
            if idx in idx_list:
                continue
            else:
                replys.append(self.reply_list[idx])

        reply_list = new_reply
        return

    def printChats(self):
        return print(self.reply_list)



reply_admin = ReplyAdmin()

while True:
    command = input()

    if '#' not in command:
        reply_admin.addChat(command)

    elif '#remove' in command:
        if '-' in command:
            num = command.split(' ')[-1]
            start = int(num.split('-')[0])
            end = int(num.split('-')[-1])

            reply_admin.removeChatRange(start, end)

        elif ',' in command:
            num = command.split(' ')[-1]
            idx_list = num.split(',')

            new_idx_list = []
            for idx in idx_list:
                new_idx_list.append(idx_list)

            idx_list = new_idx_list
            reply_admin.removeChatList(idx_list)

        else:
            idx = int(command.split(' ')[-1])
            reply_admin.removeChat(idx)
    elif '#quit' in command:
        break

    reply_admin.printChats()



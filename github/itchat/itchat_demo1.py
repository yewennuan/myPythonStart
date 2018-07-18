import itchat

if __name__ == "__main__":
    # itchat.auto_login()
    #
    # itchat.send('hello', toUserName='filehelper')

    @itchat.msg_register(itchat.content.TEXT)
    def text_reply(msg):
        return msg.text


    itchat.auto_login(hotReload=True)
    itchat.run()


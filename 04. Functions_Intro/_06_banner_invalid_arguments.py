def banner_text(text: str = ' ', width: int = 80) -> None:
    """Description:

        It formats the text which you input. It centers the string and
        it adds "**" to the beginning and end. The "text" argument must
        not be larger than "width" or 80 if you do not provide one.

        :param srt text: The text you want to format. Default = ' '.
        :param int width: Desired width, default one would be provided
               in case you have left it empty. Default = 80.
        :raise: ValueError if text is larger than width or if text is larger
                than 80 (when width arg was not provided).
        :return: It does not return anything.

    """
    if len(text) > width - 4:
        raise ValueError('String "{}" is larger than specified width {}'
                         .format(text, width))
    if text == '*':
        print('*' * width)
    else:
        output_string = '**{}**'.format(text.center(width - 4))
        print(output_string)


# stings to test the function
banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(width=60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)

import parser

def main() :
    values = ['The', 'first', 'time', 'Google', 'Photos', 'made', 'me', 'cry,', 'it', 'was', 'with', 'a', 'sucker', 'punch.', 'I', 'had', 'looked', 'at', 'my', 'phone', 'one', 'morning', 'in', 'April,', 'expecting', 'more', 'news', 'of', 'global', 'woe.', 'Instead', 'there', 'was', 'an', 'alert', 'from', 'Photos,', 'letting', 'me', 'know', 'that', 'Google', 'image-processing', 'robots', 'had', 'created', 'some', 'kind', 'of', 'montage', 'from', 'my', 'videos'
    ]

    print(parser.text2tokens(values))

main()
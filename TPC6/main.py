from parser import parser


if __name__ == "__main__":
    r = parser.parse("1 - 2 * 3")
    print(r)
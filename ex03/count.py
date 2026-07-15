import sys
import string

def text_analyzer(text=None):
    """This fuction counts the number of printable,upper,lower and punctuation characters,|
    and spaces in a given text """

    if text is None or text == "":
        text=input("What is the text to analyze?\n")

    if not isinstance(text,str):
        print("AssertionError: argument is not a string")
        return

    total_chars=len(text)
    upper_chars=0
    lower_chars=0
    punctuations=0
    spaces=0
    for char in text:
        if char.isupper():
            upper_chars+=1
        elif char.islower():
            lower_chars+=1
        elif char in string.punctuation:
            punctuation_count+=1
        elif char.isspace():
            spaces+=1

    print(f"The text contains {total_chars} printable character(s):")
    print(f"{upper_chars} upper letter(s)")
    print(f"{lower_chars} lower letter(s)")
    print(f"{punctuations} punctuation mark(s)")
    print(f"{spaces} space(s)")


if __name__ == "__main__":

    args = sys.argv[1:]
    if len(args) > 1:
        print("AssertionError: more than one argument is provided")
    elif len(args) == 1:
        text_analyzer(args[0])
    else:
        text_analyzer()
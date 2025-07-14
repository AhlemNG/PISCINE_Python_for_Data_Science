import sys

def Chars_Sum(string):
    """__doc__
    calculate  sum"""
    upper = lower = punct = digits = spaces = total = 0 
    for  character in string:
        if character in ("\n" ,"\t" ,"\r", "\f", "\v"):
            spaces +=1
        if character.isupper():
            upper +=1
        elif character.islower():
            lower +=1
        elif character.isdigit():
            digits +=1
        elif character.isspace():
            spaces +=1
        else:
            punct +=1
    print(f"The text contains {len(string)} characters:")
    print(f"{upper} upper letters") 
    print(f"{lower} lower letters") 
    print(f"{punct} punctuation marks") 
    print(f"{spaces} spaces") 
    print(f"{digits} digits") 

def main():
    """
    __doc_
    write something here"""
    args = sys.argv
    try:

        if len(args) < 2:
            raise Exception("please provide a string")
        
        Chars_Sum(args[1])
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
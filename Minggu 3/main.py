##
# Main function of the Python program.
#
##

from finder import pemenang_voting

def main():
    # we print a heading and make it bigger using HTML formatting
    print("<h4>--Pemenang Voting --</h4>")
    pemenang = pemenang_voting(["huda", "enrinal", "enrinal", "enrinal", "ivena", "huda", "enrinal", "huda", "huda" "ivena"])
    print("Pemenang voting adalah: ", pemenang)


if __name__ == '__main__':
    main()

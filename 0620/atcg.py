def comp(seq):
    comp_dict={'A':'T','T':'A','G':'C','C':'G'}
    seq_comp=""
    for char in seq:
        seq_comp+=comp_dict[char]
    return seq_comp

def rev(seq):
    seq_rev="".join(reversed(seq))
    return seq_rev

def rev_comp(seq):
    tmp=comp(seq)
    return rev(tmp)


while 1:
    print("")
    src=input("DNA 염기 서열 배열: ")
    cnvt=int(input("1(comp), 2(rev), 3(rev_comp): "))

    if cnvt==1:
        print(src,"->",comp(src))
    elif cnvt==2:
        print(src,"->",rev(src))
    elif cnvt==3:
        print(src,"->",rev_comp(src))
    else:
        print("오류")



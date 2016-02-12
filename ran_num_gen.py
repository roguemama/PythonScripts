# generate a password with length "passlen" with no duplicate characters in the password
 
import random

def random_num_gen(max_len):
    output_list = []
    count = 0
    while count < 20:
        output_list.append(random.randrange(1,max_len))
        count+=1
    random.shuffle(output_list)
    print output_list
    selector = random.randrange(0,21)
    print selector
    output = output_list[selector]
    return output

    
def get_input():
    print "What's the highest number that you want to generate?"
    max_len = raw_input()
    return max_len
    
def try_again(count2):
    print "That's not a number.  You have %s tries left." % count2
    max_len = raw_input()
    return max_len

if __name__ == '__main__':
    max_len = get_input()
    
    count2 = 5
    while count2 > 0:
        if isinstance(max_len,(int,long)) == False:
            try:
                int(max_len)
            except:
                max_len = try_again(count2)
        count2-=1
    print random_num_gen(int(max_len))

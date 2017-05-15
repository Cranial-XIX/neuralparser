import gr
import grammar
import time

def run(GrammarObject):
    grammer_obj = GrammarObject()
    t0 = time.time()
    grammer_obj.read_grammar('xbar')
    t1 = time.time()
    #print "Reading grammar takes %.4f secs" % round(t1 - t0, 5)

    print t1 - t0

    begin = time.time()
    test = "../data/corpus/test.sen"
    with open(test, 'r') as file:
        i = 0
        for sentence in file:
            if i == 1:
                break
            i += 1
            prob_sen = grammer_obj.do_inside_outside(sentence)

            #print "Inside-outside takes %.4f secs" % round(t4 - t3, 5)

            posterior_threshold = 1e-12
            grammer_obj.prune_the_chart(prob_sen, posterior_threshold)
            #t5 = time.time()
            #print "Pruning takes %.4f secs" % round(t5 - t4, 5)

            print grammer_obj.parse(sentence)
            #t6 = time.time()
            #print "Parsing takes %.4f secs\n" % round(t6 - t5, 5)

            print "log of Pr( ", sentence.strip(), ") = ", prob_sen, "\n\n"
            
            # Debug
            # grammer_obj.validate_read_grammar()


    end = time.time()
    print "Parsing takes %.4f secs\n" % round(end - begin, 5)

if __name__=="__main__":
    run(gr.GrammarObject)
    
    #run(grammar.GrammarObject)
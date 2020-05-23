import utils
from parsers import ClustalParser, MuscleParser
from matcher import AligmentDifferenceFinder

def run(inputFile, reference_id, nseq = 3):
    parser = ClustalParser(nseq) #parser.py #(quante sequenze+file) --> sequenze lette
    alignment = parser.parse(inputFile, reference=reference_id)

    print('Read {} bases'.format(len(alignment)))
    analyzer = AligmentDifferenceFinder()
    groups = analyzer.analyze(alignment)
    utils.save(alignment, analyzer, path='output', reference_id = reference_id)

def main():
    #get id of reference sequence
    reference_id = open("input/reference.fasta", "r").readline().split(' ')[0][1:] # NC_045512.2

    # Muscle Parser
    muscle_parser = MuscleParser(nseq=8)  #parser.py #(quante sequenze+file) --> sequenze lette
    muscle_alignment = muscle_parser.parse('analysis/muscle-I20200512-170208-0225-69454386-p1m.clw', reference=reference_id)

    print('Read {} bases'.format(len(muscle_alignment)))
    analyzer = AligmentDifferenceFinder() # matcher.py
    groups = analyzer.analyze(muscle_alignment) # vettori indici mismatch rispetto al reference per sequenza
    utils.save(muscle_alignment, analyzer, path='output', reference_id=reference_id)

    # Clustal Parser iran
    run('analysis/iran-ref.txt', reference_id, 3)

    # Muscle Parser iran
    muscle_parser = MuscleParser(nseq=3)  #parser.py #(quante sequenze+file) --> sequenze lette
    muscle_alignment = muscle_parser.parse('analysis/muscle-I20200523-084930-0610-44096621-p1m.clw', reference=reference_id)

    print('Read {} bases'.format(len(muscle_alignment)))
    analyzer = AligmentDifferenceFinder() # matcher.py
    groups = analyzer.analyze(muscle_alignment) # vettori indici mismatch rispetto al reference per sequenza
    utils.save(muscle_alignment, analyzer, path='output', reference_id=reference_id)
    #run('analysis/muscle-I20200523-084930-0610-44096621-p1m.clw', reference_id, 4)

    # Clustal Parser israel
    run('analysis/israel-ref.txt', reference_id, 3)

    # Muscle Parser israel
    muscle_parser = MuscleParser(nseq=4)  #parser.py #(quante sequenze+file) --> sequenze lette
    muscle_alignment = muscle_parser.parse('analysis/muscle-I20200523-085708-0753-28920419-p1m.clw', reference=reference_id)

    print('Read {} bases'.format(len(muscle_alignment)))
    analyzer = AligmentDifferenceFinder() # matcher.py
    groups = analyzer.analyze(muscle_alignment) # vettori indici mismatch rispetto al reference per sequenza
    utils.save(muscle_alignment, analyzer, path='output', reference_id=reference_id)
    #run('analysis/muscle-I20200523-085708-0753-28920419-p1m.clw', reference_id, 3)

    #Clustal Parser ncbi
    run('analysis/all.txt', reference_id, 3)

    # Muscle Parser ncbi
    muscle_parser = MuscleParser(nseq=8)  #parser.py #(quante sequenze+file) --> sequenze lette
    muscle_alignment = muscle_parser.parse('analysis/muscle-I20200512-170208-0225-69454386-p1m.clw', reference=reference_id)

    print('Read {} bases'.format(len(muscle_alignment)))
    analyzer = AligmentDifferenceFinder() # matcher.py
    groups = analyzer.analyze(muscle_alignment) # vettori indici mismatch rispetto al reference per sequenza
    utils.save(muscle_alignment, analyzer, path='output', reference_id=reference_id)
    #run('analysis/muscle-I20200512-170208-0225-69454386-p1m.clw', reference_id, 3)

    # Clustal Global Parser
    run('analysis/global.txt', reference_id, 14)

    # Muscle Global Parser
    muscle_parser = MuscleParser(nseq=15)  #parser.py #(quante sequenze+file) --> sequenze lette
    muscle_alignment = muscle_parser.parse('analysis/muscle-I20200523-090837-0910-95910164-p1m.clw', reference=reference_id)

    print('Read {} bases'.format(len(muscle_alignment)))
    analyzer = AligmentDifferenceFinder() # matcher.py
    groups = analyzer.analyze(muscle_alignment) # vettori indici mismatch rispetto al reference per sequenza
    utils.save(muscle_alignment, analyzer, path='output', reference_id=reference_id)
    #run('analysis/muscle-I20200523-090837-0910-95910164-p1m.clw', reference_id, 14)


if __name__ == "__main__":
    main()

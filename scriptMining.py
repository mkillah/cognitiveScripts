def is_consecutive_subsequence(subsequence:list, sequence:list) -> bool:
    '''
    c
    :param subsequence: list of attributes
    :param sequence: list of attributes
    :return: bool
    '''
    
    sub_len = len(subsequence)
    seq_len = len(sequence)

    if sub_len > seq_len:
        return False

    for i in range(seq_len - sub_len + 1):
        if sequence[i:i + sub_len] == subsequence:
            return True

    return False

def seqMining(seq1:list, seq2:list) -> list:
    '''
    The function is used to mine a script, a sequence of the successive list of attributes.
    :param seq1: list of attributes
    :param seq2: list of attributes
    :return: all successive chunks as intersection of input lists
    '''

    minedSeqs = []

    for n in seq1:
        # setting and re-setting indHelper
        indHelper = seq1.index(n)
        chunks = []
        subsequence = [n]
        while is_consecutive_subsequence(subsequence, seq2):

            # get only subsequence that has number of elements greater than 1
            if len(subsequence) > 1:
                chunks.append(subsequence)

            # adding an index to relative indHelper
            indHelper += 1

            # if there is next element of sequence
            if indHelper <= len(seq1) - 1:
                nextElem = seq1[indHelper]
                subsequence = subsequence + [nextElem]  # extend subsequence
            else:
                break
        for chunk in chunks:
            if (len(chunk) > 0) and (chunk not in minedSeqs):
                minedSeqs.append(chunk)

    return minedSeqs

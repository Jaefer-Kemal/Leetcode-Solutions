class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # First lets sort the citations:
        citations.sort()

        no_of_paper = len(citations)
        
        maximum_h_index = 0

        citations_dict = {}

        for i in range(0, no_of_paper):
            if citations[i] not in citations_dict and citations[i]:
                number_of_citation = no_of_paper - i 
                citations_dict[citations[i]] = number_of_citation
        
        for citation, paper in citations_dict.items():
            if citation <= paper:
                maximum_h_index = max(citation, maximum_h_index)
            else:
                maximum_h_index = max(paper, maximum_h_index)
                
        return maximum_h_index
            
            

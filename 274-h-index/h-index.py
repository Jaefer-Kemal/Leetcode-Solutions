class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # First lets sort the citations:
        citations.sort()

        # Total number of paper 
        total_papers = len(citations)
        
        maximum_h_index = 0

        # A dictionary to store remaining paper with at least k citations
        # {citation : no_of_paper}
        citations_paper_count = {}

        for i in range(0, total_papers):
            if citations[i] not in citations_paper_count:
                remaining_papers = total_papers - i 
                citations_paper_count[citations[i]] = remaining_papers
        
        for citation, paper in citations_paper_count.items():
            if citation <= paper:
                maximum_h_index = max(citation, maximum_h_index)
            else:
                maximum_h_index = max(paper, maximum_h_index)
                
        return maximum_h_index
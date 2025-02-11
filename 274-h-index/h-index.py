class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        total_papers = len(citations) + 1
        # Lets Sort it using Counting sort
        count_arr=  [0] * total_papers

        for citation in citations:
            if citation >= total_papers:
                count_arr[-1] += 1
            else:
                count_arr[citation] += 1

        for i in range(total_papers - 2, -1, -1):
            count_arr[i] += count_arr[i + 1]
        
        h_index = 0
        for i in range(total_papers - 1, -1, -1):
            if i <= count_arr[i]:
                return i 

        # # First lets sort it according to the number of citations in each paper
        # citations.sort()

        # # Total number of paper 
        # total_papers = len(citations)
        
        # maximum_h_index = 0

        # # A dictionary to store remaining paper with at least k citations
        # # {citation : no_of_paper}
        # citations_paper_count = {}

        # for i in range(0, total_papers):
        #     if citations[i] not in citations_paper_count:
        #         remaining_papers = total_papers - i 
        #         citations_paper_count[citations[i]] = remaining_papers
        
        # for citation, paper in citations_paper_count.items():
        #     if citation <= paper:
        #         maximum_h_index = max(citation, maximum_h_index)
        #     else:
        #         maximum_h_index = max(paper, maximum_h_index)
                
        # return maximum_h_index
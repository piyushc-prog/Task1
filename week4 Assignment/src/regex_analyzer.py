import re

class RegexAnalyzer:
    
    def extract_dates(self, text):
        patterns = [
            r"\d{2}/\d{2}/\d{4}",
            r"\d{2}-\d{2}-\d{4}",
            r"\w+ \d{1,2}, \d{4}"
        ]
        
        dates = []
        for p in patterns:
            dates += re.findall(p, text)
        
        return dates
    
    def extract_money(self, text):
        return re.findall(r"\$\d+(?:,\d+)*(?:\.\d+)?", text)
    
    def extract_percent(self, text):
        return re.findall(r"\d+%", text)
    
    def extract_time_phrases(self, text):
        return re.findall(r"\b\w+ (years|months|minutes)\b", text)
import random

class OutfitRecommendationModel:
    def __init__(self):
        self.categories = ['tops', 'bottoms', 'shoes', 'accessories']

    def recommend(self, wardrobe_items):
        outfit = {}
        for category in self.categories:
            items = [item for item in wardrobe_items if item['category'] == category]
            if items:
                outfit[category] = random.choice(items)
        return outfit
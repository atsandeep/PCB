class PCBuilder:
    def __init__(self):
        self.specifications = {}
        self.intel_processors = ["Intel i9-11900K", "Intel i7-12700K", "Intel i5-11600K"]
        self.amd_processors = ["AMD Ryzen 9 5950X", "AMD Ryzen 7 5800X", "AMD Ryzen 5 5600X"]
        self.dollar_to_rupee_conversion_rate = 75.0  # You can adjust the conversion rate as needed
        self.graphics_card_recommendations = {
            (0, 25000): "Integrated Graphics (e.g., Intel UHD Graphics, AMD Radeon Graphics)",
            (25001, 50000): "NVIDIA GTX 1650 or AMD RX 5500 XT",
            (50001, 100000): "NVIDIA RTX 3060 or AMD RX 6700 XT",
            (100001, 150000): "NVIDIA RTX 3070 or AMD RX 6800",
            (150001, 200000): "NVIDIA RTX 3080 or AMD RX 6900 XT",
            (200001, float('inf')): "NVIDIA RTX 3090 or AMD RX 6900 XT (for enthusiasts)"
        }

    def get_user_requirements(self):
        print("Welcome to the PC Builder!")
        print("Please answer the following questions to help us understand your requirements.")

        self.specifications['budget'] = float(input("1. What is your budget? ₹"))
        self.specifications['usage'] = input("2. What will you use the PC for? (e.g., gaming, video editing, programming): ").lower()
        self.specifications['storage'] = input("3. Do you need a large amount of storage? (yes/no): ").lower()

        if self.specifications['storage'] == 'yes':
            self.specifications['storage_type'] = input("4. Do you prefer SSD or HDD for storage? (ssd/hdd): ").lower()

        self.specifications['graphics_card'] = input("5. Do you need a dedicated graphics card? (yes/no): ").lower()
        self.specifications['processor_preference'] = input("6. Do you have a preference for Intel or AMD processors? (intel/amd/none): ").lower()

    def categorize_user(self):
        if 0 <= self.specifications['budget'] <= 25000:
            return "Low-End User"
        elif 40000 <= self.specifications['budget'] <= 75000:
            return "Medium-End User"
        elif 75000 <= self.specifications['budget'] <= 600000:
            return "High-End User"
        else:
            return "Undefined User"

    def get_graphics_card_recommendation(self, budget):
        for price_range, recommendation in self.graphics_card_recommendations.items():
            if price_range[0] <= budget <= price_range[1]:
                return recommendation

    def build_pc(self):
        print("\nBased on your requirements, here's a suggested PC configuration:")

        print(f"\nBudget: ₹{self.specifications['budget']:.2f}")
        print(f"User Category: {self.categorize_user()}")

        user_category = self.categorize_user()

        if user_category != "Undefined User":
            if self.specifications['usage'] == 'gaming':
                print("For gaming, we recommend a powerful CPU and a dedicated graphics card.")
                graphics_card_recommendation = self.get_graphics_card_recommendation(self.specifications['budget'])
                print(f"Graphics Card Recommendation: {graphics_card_recommendation}")

                # Sample motherboard and RAM suggestions (customize based on actual components)
                if user_category == "High-End User":
                    print("Motherboard: High-end gaming motherboard (e.g., ASUS ROG Strix Z590)")
                    print("RAM: 32GB or 64GB DDR4 3400MHz - 4500MHz")

                elif user_category == "Medium-End User":
                    print("Motherboard: Mid-range gaming motherboard (e.g., MSI B450 TOMAHAWK MAX)")
                    print("RAM: 16GB DDR4 3400MHz")

                elif user_category == "Low-End User":
                    print("Motherboard: Entry-level gaming motherboard (e.g., ASRock B450M-HDV R4.0)")
                    print("RAM: 8GB DDR4 2400MHz - 3400MHz")

            elif self.specifications['usage'] == 'video editing':
                print("For video editing, consider a powerful CPU and additional RAM for smooth performance.")
                graphics_card_recommendation = self.get_graphics_card_recommendation(self.specifications['budget'])
                print(f"Graphics Card Recommendation: {graphics_card_recommendation}")

                # Sample motherboard and RAM suggestions (customize based on actual components)
                if user_category == "High-End User":
                    print("Motherboard: High-end video editing motherboard (e.g., ASUS ProArt B550-CREATOR)")
                    print("RAM: 32GB or 64GB DDR4 3400MHz - 4500MHz")

                elif user_category == "Medium-End User":
                    print("Motherboard: Mid-range video editing motherboard (e.g., MSI MAG B550 TOMAHAWK)")
                    print("RAM: 16GB DDR4 3400MHz")

                elif user_category == "Low-End User":
                    print("Motherboard: Entry-level video editing motherboard (e.g., ASRock B450M Pro4)")
                    print("RAM: 8GB DDR4 2400MHz - 3400MHz")

            elif self.specifications['usage'] == 'programming':
                print("For programming, a balanced configuration with a decent CPU and sufficient RAM is recommended.")

                # Sample motherboard and RAM suggestions (customize based on actual components)
                if user_category == "High-End User" or user_category == "Medium-End User":
                    print("Motherboard: Mid-range programming motherboard (e.g., ASUS PRIME B450M-A)")
                    print("RAM: 16GB DDR4 3400MHz")

                elif user_category == "Low-End User":
                    print("Motherboard: Entry-level programming motherboard (e.g., ASRock B450M-HDV R4.0)")
                    print("RAM: 8GB DDR4 2400MHz - 3400MHz")

            else:
                print(f"We recommend a general-purpose configuration for {self.specifications['usage']}.")

            if self.specifications['storage'] == 'yes':
                print(f"Storage Type: {self.specifications['storage_type'].upper()}")

                if self.specifications['storage_type'] == 'ssd':
                    print("SSD Options:")

                    # Sample SSD options based on budget (customize based on actual components)
                    if user_category == "High-End User":
                        print("1. Samsung 970 EVO Plus 1TB")
                        print("2. WD Black SN850 1TB")
                        print("3. Kingston KC2500 1TB")

                    elif user_category == "Medium-End User":
                        print("1. Crucial P5 500GB")
                        print("2. Kingston A2000 500GB")
                        print("3. WD Blue SN550 500GB")

                    elif user_category == "Low-End User":
                        print("1. Kingston A2000 250GB")
                        print("2. WD Green 240GB")
                        print("3. Crucial BX500 240GB")

                elif self.specifications['storage_type'] == 'hdd':
                    print("HDD Options:")

                    # Sample HDD options based on budget (customize based on actual components)
                    if user_category == "High-End User":
                        print("1. Seagate Barracuda 2TB")
                        print("2. WD Black 2TB")
                        print("3. Toshiba X300 2TB")

                    elif user_category == "Medium-End User":
                        print("1. Seagate Barracuda 1TB")
                        print("2. WD Blue 1TB")
                        print("3. Toshiba P300 1TB")

                    elif user_category == "Low-End User":
                        print("1. Seagate Barracuda 500GB")
                        print("2. WD Blue 500GB")
                        print("3. Toshiba P300 500GB")

            if self.specifications['graphics_card'] == 'yes':
                print("A dedicated graphics card will enhance your system's graphics performance.")

            if self.specifications['processor_preference'] == 'intel':
                print("Consider an Intel processor for optimal performance.")
                print("Available Intel processors:")
                for processor in self.intel_processors:
                    print(f"- {processor}")

                # Sample motherboard suggestions for Intel (customize based on actual components)
                if user_category == "High-End User":
                    print("Motherboard Options:")
                    print("1. ASUS ROG Strix Z590")
                    print("2. MSI MPG B560 GAMING EDGE WIFI")

                elif user_category == "Medium-End User":
                    print("Motherboard Options:")
                    print("1. MSI MAG B450 TOMAHAWK MAX")
                    print("2. ASUS PRIME B460M-A")

                elif user_category == "Low-End User":
                    print("Motherboard Options:")
                    print("1. ASRock B450M-HDV R4.0")
                    print("2. ASUS Prime H410M-E")

            elif self.specifications['processor_preference'] == 'amd':
                print("Consider an AMD processor for a cost-effective and powerful option.")
                print("Available AMD processors:")
                for processor in self.amd_processors:
                    print(f"- {processor}")

                # Sample motherboard suggestions for AMD (customize based on actual components)
                if user_category == "High-End User":
                    print("Motherboard Options:")
                    print("1. ASUS ProArt B550-CREATOR")
                    print("2. MSI MPG B550 GAMING PLUS")

                elif user_category == "Medium-End User":
                    print("Motherboard Options:")
                    print("1. MSI MAG B550 TOMAHAWK")
                    print("2. ASUS TUF B450M-PLUS GAMING")

                elif user_category == "Low-End User":
                    print("Motherboard Options:")
                    print("1. ASRock B450M Pro4")
                    print("2. Gigabyte B450M DS3H")

                print("We'll provide recommendations based on your other requirements.")

            # Caution message for budget mismatch
            if (user_category == "Low-End User" and not 0 <= self.specifications['budget'] <= 25000) or \
               (user_category == "Medium-End User" and not 40000 <= self.specifications['budget'] <= 75000) or \
               (user_category == "High-End User" and not 75000 <= self.specifications['budget'] <= 600000):
                print("\nCaution: It seems that the specified budget may not align with the selected usage or preferences.")
                print("You might be paying more for certain specifications than necessary.")

        else:
            print("Undefined User: Please provide a valid budget within the specified ranges.")

        print("\nThank you for using the PC Builder!")

if __name__ == "__main__":
    pc_builder = PCBuilder()
    pc_builder.get_user_requirements()
    pc_builder.build_pc()
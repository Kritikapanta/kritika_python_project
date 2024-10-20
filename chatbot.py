# chatbot.py
import re
from fuzzywuzzy import process

questions = {
        ("hi", "hello", "greetings","good morning", "good night", "good evening"): "Hello! How can I help you today?",
        "hi":"Hello! How can I help you today?",
        "hello":"Hello! How can I help you today?",
        "how are you?": "I'm fine, how about you?",
        ("bye", "good bye"): "Goodbye! Have a great day!",
        ("what is the best facial treatment for oily skin?", "facial oily skin", "facial for oily skin"):"For oily skin, we recommend a deep-cleansing facial that incorporates clay or charcoal masks. These ingredients are excellent for absorbing excess oil and unclogging pores. Additionally, our facials include salicylic acid, which helps prevent breakouts and control shine, leaving your skin refreshed and balanced.",
        "What facial is recommended for sensitive skin?":"For sensitive skin, we offer a calming and soothing facial treatment. We focus on using gentle ingredients like aloe vera, chamomile, and cucumber, which effectively reduce redness and irritation. Our facials are designed to avoid harsh exfoliants and fragrances, ensuring a comfortable experience while deeply hydrating and repairing your skin’s barrier.",
        "What facial treatment works best for dry skin?":"If you have dry skin, our hydrating facial is perfect for you. This treatment includes rich moisturizers, hyaluronic acid, and nourishing oils like jojoba and argan oil. We focus on replenishing moisture and enhancing your skin’s barrier function, leaving your skin feeling soft, revitalized, and deeply nourished.",
        "What facial is suitable for normal skin?":"For normal skin, we recommend a balanced facial that promotes overall health and radiance. Our treatments include gentle exfoliation, hydration, and antioxidants. We use ingredients like vitamins C and E, along with lightweight moisturizers, to maintain balance and enhance your skin's natural glow.",
        ("How can I get discounts", "Are there discounts?", "I want discount"):"You can refer you friends to get special discounts.",
        "What is the best facial for mixed skin?":"For mixed skin, we provide a customized facial that addresses the unique needs of both oily and dry areas. Our treatment incorporates a combination of exfoliating products for oilier zones, like the T-zone, and hydrating products for drier areas, such as the cheeks. A balancing facial with clay masks and moisturizing serums effectively caters to your skin's diverse requirements, ensuring you leave with a balanced and healthy complexion.",
        "What will be suitable facial for oily skin":"For oily skin, we recommend our Deep Cleansing Facial or the Charcoal Detox Facial, both designed to remove excess oil and impurities.",
        "do you provide hair treatments?": "Yes, we offer various hair treatments including haircuts, coloring, styling, and specialized treatments like keratin therapy and deep conditioning.",
        "can i book a manicure appointment?": "Yes, you can easily book a manicure appointment. You can do so online or by calling us directly.",
        "what facials do you recommend for oily skin?": "For oily skin, we recommend our Deep Cleansing Facial or the Charcoal Detox Facial, both designed to remove excess oil and impurities.",
        "do you have bridal makeup services?": "Yes, we provide full bridal makeup services starting from Rs. 25,000. Our services include trials, hair styling, and makeup to give you the perfect look for your big day.",
        "what skincare products do you use?": "We use high-quality skincare products from brands like Dermalogica, Neutrogena, and The Body Shop, known for their effectiveness and safety.",
        "do you sell beauty products in your studio?": "Yes, we sell a curated range of skincare and haircare products at our studio.",
        "can i purchase hair care products online?": "Currently, we do not offer online purchases for hair care products, but you can buy them directly from our studio.",
        "do you have organic or cruelty-free products?": "Yes, we carry a selection of organic and cruelty-free products, including some skincare and haircare options.",
        "how can i book an appointment?": "You can book an appointment through our website, by calling us, or through our social media pages.",
        "what is your availability for next week?": "Please check our online booking system for the latest availability, or you can call us, and we will let you know our open slots.",
        "can i reschedule my appointment?": "Yes, you can reschedule your appointment by contacting us at least 24 hours before your scheduled time.",
        "do you offer online bookings?": "Yes, we offer online bookings through our website.",
        "What is price for bridal makeup":"For bridal makeup we startig price of 25000. The bridal makeup package includes a trial session, hair styling, makeup, and on-the-day touch-ups to ensure everything looks perfect.",
        "what are your service prices?": "Our basic services start from Rs. 500, with bridal packages priced at Rs. 25,000. Hair treatments range from Rs. 1,000 to Rs. 15,000, while specialized services like spa and body treatments range up to Rs. 30,000.",
        "do you have any current offers or discounts?": "Yes, we have seasonal promotions and discounts for first-time clients. Please check our website or contact us for the latest deals.",
        "what is the price for a haircut?": "Haircuts start from Rs. 1,000, depending on the style and treatment you choose.",
        "are there any packages for beauty treatments?": "Yes, we offer various packages, including bridal packages and spa bundles that combine facials, massages, and hair treatments.",
        "what are your opening hours?": "We are open from 10 AM to 7 PM, Monday through Saturday.",
        "where is your beauty studio located?": "We are located in Baneshwor, Kathmandu, near the Baneshwor Chowk.",
        "do you offer waxing services?": "Yes, we offer a range of waxing services, including full body waxing, facial waxing, and specific areas like arms, legs, and bikini waxing.",
        "do you offer eyebrow threading and tinting?": "Yes, we offer professional eyebrow threading and tinting services to give your brows a perfect shape and color.",
        "what massage treatments do you provide?": "We offer a variety of massage treatments, including full body massages, deep tissue massages, and relaxation massages.",
        "can i book a spa package?": "Yes, we offer spa packages that combine facials, massages, and body treatments for a complete rejuvenation experience.",
        "do you have party makeup services?": "Yes, we offer party and event makeup services to help you look your best for any occasion.",
        "what products do you use for hair coloring?": "We use professional-grade products from brands like L'Oréal, Schwarzkopf, and Wella for all our hair coloring services.",
        "do you provide skincare consultations?": "Yes, we provide skincare consultations to help you choose the right treatments and products for your skin type.",
        "how can i pay for services?": "You can pay for services via cash, card, or mobile payment apps such as eSewa and Khalti.",
        "do you offer gift cards?": "Yes, we offer gift cards that you can purchase for friends and family. They make great presents!",
        "do you provide nail art services?": "Yes, we offer nail art services along with our manicures and pedicures. You can choose from a variety of designs.",
        "what are the prices for spa treatments?": "Our spa treatments start from Rs. 3,000 and can go up to Rs. 30,000 depending on the type of treatment you choose.",
        "do you offer hair spa services?": "Yes, we offer hair spa services to rejuvenate and nourish your hair with treatments designed for different hair types.",
        "what is the cost of eyebrow tinting?": "Eyebrow tinting costs Rs. 1,500, and you can combine it with threading for a discounted price of Rs. 2,000.",
        "do you have special offers for bridal packages?": "Yes, we offer customized bridal packages with discounts if you book both pre-bridal and bridal services together.",
        "can i get a same-day appointment?": "Same-day appointments are subject to availability. Please call us to check for open slots.",
        "do you offer male grooming services?": "Yes, we offer grooming services for men, including haircuts, facials, and waxing.",
        "what is included in the bridal makeup package?": "The bridal makeup package includes a trial session, hair styling, makeup, and on-the-day touch-ups to ensure everything looks perfect.",
        "do you offer membership programs?": "Yes, we have membership programs where you can enjoy discounted rates on services and special perks for frequent clients.",
        "can i bring my own products for treatments?": "Yes, you can bring your own products if you prefer. Just let our team know beforehand so we can accommodate your request.",
        "do you offer skincare treatments for acne?": "Yes, we offer specialized skincare treatments for acne, including our anti-acne facial and chemical peels designed to reduce inflammation and clear pores.",
        "do you have anti-aging treatments?": "Yes, we offer anti-aging treatments like our collagen-boosting facials and microneedling, which help improve skin elasticity and reduce fine lines.",
        "can i request a specific beautician?": "Yes, you can request a specific beautician when booking your appointment, subject to their availability.",
        "do you offer group packages for parties?": "Yes, we offer group packages for bridal parties, birthdays, and other special occasions. Please contact us for more details.",
        "what are your hygiene and safety measures?": "We follow strict hygiene and safety protocols, including sanitizing equipment, using disposable tools where possible, and ensuring all staff wear masks and gloves.",
        "do you offer makeup tutorials?": "Yes, we offer one-on-one and group makeup tutorials where you can learn how to apply makeup like a pro.",
        "can i get a discount for referring a friend?": "Yes, we offer referral discounts where both you and your friend can enjoy a 10% discount on your next service.",
        "what hair removal methods do you offer?": "We offer waxing, threading, and laser hair removal for different parts of the body.",
        "what are your payment methods?": "We accept cash, credit/debit cards, and mobile payments such as eSewa and Khalti.",
        "do you offer piercings?": "Yes, we offer ear piercings using sterilized equipment to ensure safety and hygiene.",
        "can i purchase gift vouchers online?": "Currently, gift vouchers can be purchased in-store only. However, we are working to make them available online soon.",
        "do you offer makeup for special events?": "Yes, we provide makeup services for special events such as parties, proms, and corporate functions.",
        "can i bring a friend with me to my appointment?": "Yes, you're welcome to bring a friend with you to your appointment.",
        "do you have services for sensitive skin?": "Yes, we offer a range of treatments specifically designed for sensitive skin, using hypoallergenic products.",
        "what is the duration of a facial?": "Facial treatments typically last between 60 to 90 minutes, depending on the type of facial you choose.",
        "can i cancel my appointment?": "Yes, you can cancel your appointment, but we kindly request that you notify us at least 24 hours in advance.",
        "do you offer free consultations?": "Yes, we offer free consultations for skincare, haircare, and makeup services to help you choose the right treatments.",
        "what is price for facial services?": (
        "Price for facial services:\n"
        "Hydra Facial: Rs 2500\n"
        "Classic Facial: Rs 1500\n"
        "Anti-Aging Facial: Rs 4500\n"
        "Acne Treatment Facial: Rs 4000\n"
        "Brightening Facial: Rs 5000\n"
        "Deep Cleansing Facial: Rs 1800\n"
        "Soothing Facial for Sensitive Skin: Rs 2400\n"
        "Brightening Peel Treatment: Rs 2000\n"
        "Microdermabrasion: Rs 5000\n"
        "Signature Spa Facial: Rs 3500\n"
        "Collagen Facial: Rs 3200\n"
        "Express Facial: Rs 1000\n"
        "Back Facial: Rs 1800\n"
        "LED Light Therapy Facial: Rs 8000\n"
        "Detoxifying Clay Mask Facial: Rs 2300\n"
        "Hydrating Facial: Rs 2600\n"
        "Balancing Facial: Rs 2200\n"
        "Calming Facial: Rs 2400"),
        "what is the price for cleansing?":"Price for cleansing: Rs 700",
        "what is the price for threading?":"Price for eyebrows threading: Rs 50",
        ("what is the price for thinning the eyebrow?", "how much do you charge for eyebrow shaping?", "what is the price for eyebrow tinting?"):"Price for eyebrows threading: Rs 50",
        ("what services do you offer?", "Your services", "Can I get the list of the serviecs you offer", "list of your services"): (
        "We offer a variety of beauty services including:\n"
        "Hair treatments (cutting, coloring, styling)\n"
        "Facials (for different skin types)\n"
        "Manicures and Pedicures\n"
        "Bridal Makeup Services\n"
        "Party and Event Makeup\n"
        "Skincare Treatments\n"
        "Eyebrow Threading and Tinting\n"
        "Waxing and Hair Removal\n"
        "Body Spa and Massage.")
        
    }
    
    # Normalize input function
def normalize_input(user_input):
    user_input = user_input.lower()  # Convert to lowercase
    user_input = re.sub(r'\s+', ' ', user_input)  # Remove extra spaces
    user_input = user_input.strip()  # Strip leading/trailing spaces
    return user_input

def get_response(user_input):
    normalized_input = normalize_input(user_input)
    
    # Find the closest matching question
    matched_question, _ = process.extractOne(normalized_input, questions.keys())

    # Check if the match is close enough (e.g., above a threshold score)
    if matched_question and process.extractOne(normalized_input, questions.keys())[1] > 80:  # You can adjust the score threshold
        return questions[matched_question]
    
    return "Thank you for leaving your message. We will contact you soon."

if __name__ == "__main__":
    print("Welcome to the Beauty Studio Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)
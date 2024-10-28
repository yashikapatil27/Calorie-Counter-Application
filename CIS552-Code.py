import pymongo
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.image import Image
from datetime import datetime
from bson import ObjectId
import hashlib
from kivy.uix.screenmanager import ScreenManager, FadeTransition


# Establish connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["calorie_counter"]
meals_collection = db["meals"]
food_db_collection = db["food_database"]
users_collection = db["users"]

# Initialize food database if it's empty
if food_db_collection.count_documents({}) == 0:
    common_foods = [
        {"name": "Apple", "calories": 95},
        {"name": "Banana", "calories": 105},
        {"name": "Chicken Breast (100g)", "calories": 165},
        {"name": "Whole Wheat Bread (1 slice)", "calories": 69},
        {"name": "Egg", "calories": 78},
        {"name": "Rice (1 cup cooked)", "calories": 205},
        {"name": "Salmon (100g)", "calories": 208},
        {"name": "Spinach (1 cup)", "calories": 7},
        {"name": "Pasta (1 cup cooked)", "calories": 221},
        {"name": "Cheeseburger", "calories": 303},
        {"name": "Pizza (1 slice)", "calories": 285},
        {"name": "French Fries (medium)", "calories": 365},
        {"name": "Hot Dog", "calories": 150},
        {"name": "Bacon (1 slice)", "calories": 42},
        {"name": "Peanut Butter (2 tbsp)", "calories": 188},
        {"name": "Chocolate Chip Cookie", "calories": 78},
        {"name": "Ice Cream (1 cup)", "calories": 273},
        {"name": "Grilled Cheese Sandwich", "calories": 300},
        {"name": "Pancakes (2 medium)", "calories": 180},
        {"name": "Granola Bar", "calories": 120},
        {"name": "Beef Steak (100g)", "calories": 271},
        {"name": "Taco", "calories": 170},
        {"name": "Bagel", "calories": 250},
        {"name": "Yogurt (1 cup)", "calories": 150},
        {"name": "Cereal (1 cup)", "calories": 110},
        {"name": "Oatmeal (1 cup cooked)", "calories": 154},
        {"name": "Popcorn (1 cup)", "calories": 31},
        {"name": "Potato Chips (1 oz)", "calories": 152},
        {"name": "Muffin", "calories": 340},
        {"name": "Lasagna", "calories": 336},
        {"name": "Chicken Nugget (1 piece)", "calories": 45},
        {"name": "Macaroni and Cheese (1 cup)", "calories": 310},
        {"name": "Sub Sandwich", "calories": 500},
        {"name": "BBQ Ribs (100g)", "calories": 250},
        {"name": "Baked Potato (medium)", "calories": 161},
        {"name": "Pork Chop (100g)", "calories": 231},
        {"name": "Sausage (1 link)", "calories": 200},
        {"name": "Waffles (2 pieces)", "calories": 218},
        {"name": "Brownie", "calories": 132},
        {"name": "Corn on the Cob (1 ear)", "calories": 77},
        {"name": "Tuna Salad (1 cup)", "calories": 383},
        {"name": "Caesar Salad (1 cup)", "calories": 180},
        {"name": "Roast Beef (100g)", "calories": 250},
        {"name": "Clam Chowder (1 cup)", "calories": 200},
        {"name": "Garlic Bread (1 slice)", "calories": 150},
        {"name": "Pancake Syrup (2 tbsp)", "calories": 110},
        {"name": "Cupcake", "calories": 200},
        {"name": "Buffalo Wings (1 piece)", "calories": 90},
        {"name": "Beef Burrito", "calories": 290},
        {"name": "Cottage Cheese (1 cup)", "calories": 206},
        {"name": "Quiche (1 slice)", "calories": 300},
        {"name": "Eggplant Parmesan (1 cup)", "calories": 366},
        {"name": "Stuffed Peppers (1 piece)", "calories": 200},
        {"name": "Fried Rice (1 cup)", "calories": 238},
        {"name": "Spring Roll (1 piece)", "calories": 100},
        {"name": "Miso Soup (1 cup)", "calories": 84},
        {"name": "Pad Thai (1 cup)", "calories": 400},
        {"name": "Sushi Roll (1 roll)", "calories": 250},
        {"name": "Dim Sum (1 piece)", "calories": 100},
        {"name": "Fish Tacos (2 pieces)", "calories": 300},
        {"name": "Falafel (1 piece)", "calories": 57},
        {"name": "Hummus (2 tbsp)", "calories": 50},
        {"name": "Pita Bread (1 piece)", "calories": 165},
        {"name": "Gyro Sandwich", "calories": 600},
        {"name": "Baklava (1 piece)", "calories": 334},
        {"name": "Pho (1 bowl)", "calories": 350},
        {"name": "Ramen (1 bowl)", "calories": 436},
        {"name": "Kebab (1 skewer)", "calories": 200},
        {"name": "Tofu (100g)", "calories": 76},
        {"name": "Broccoli (1 cup)", "calories": 55},
        {"name": "Carrot (1 medium)", "calories": 25},
        {"name": "Almonds (1 oz)", "calories": 164},
        {"name": "Avocado (1 medium)", "calories": 234},
        {"name": "Blueberries (1 cup)", "calories": 84},
        {"name": "Greek Yogurt (1 cup)", "calories": 100},
        {"name": "Turkey Breast (100g)", "calories": 104},
        {"name": "Sweet Potato (1 medium)", "calories": 103},
        {"name": "Quinoa (1 cup cooked)", "calories": 222},
        {"name": "Kale (1 cup)", "calories": 33},
        {"name": "Mango (1 medium)", "calories": 201},
        {"name": "Chia Seeds (1 oz)", "calories": 138},
        {"name": "Beef Jerky (1 oz)", "calories": 116},
        {"name": "Cashews (1 oz)", "calories": 157},
        {"name": "Edamame (1 cup)", "calories": 188},
        {"name": "Shrimp (100g)", "calories": 99},
        {"name": "Green Beans (1 cup)", "calories": 31},
        {"name": "Lentils (1 cup cooked)", "calories": 230},
        {"name": "Black Beans (1 cup cooked)", "calories": 227},
        {"name": "Pomegranate (1 medium)", "calories": 234},
        {"name": "Raspberries (1 cup)", "calories": 64},
        {"name": "Cauliflower (1 cup)", "calories": 25},
        {"name": "Cabbage (1 cup)", "calories": 22},
        {"name": "Brussels Sprouts (1 cup)", "calories": 38},
        {"name": "Grapefruit (1 medium)", "calories": 52},
        {"name": "Orange (1 medium)", "calories": 62},
        {"name": "Pineapple (1 cup)", "calories": 82},
        {"name": "Cucumber (1 medium)", "calories": 45},
        {"name": "Peas (1 cup)", "calories": 118},
        {"name": "Chickpeas (1 cup cooked)", "calories": 269},
        {"name": "Coconut Water (1 cup)", "calories": 46},
        {"name": "Tomato (1 medium)", "calories": 22},
        {"name": "Bell Pepper (1 medium)", "calories": 24},
        {"name": "Zucchini (1 cup)", "calories": 20},
        {"name": "Pumpkin Seeds (1 oz)", "calories": 126},
        {"name": "Sunflower Seeds (1 oz)", "calories": 165},
        {"name": "Cranberries (1 cup)", "calories": 46},
        {"name": "Pear (1 medium)", "calories": 101},
        {"name": "Peach (1 medium)", "calories": 59},
        {"name": "Plum (1 medium)", "calories": 30},
        {"name": "Raisins (1 oz)", "calories": 85},
        {"name": "Watermelon (1 cup)", "calories": 46},
        {"name": "Honeydew Melon (1 cup)", "calories": 64},
        {"name": "Cantaloupe (1 cup)", "calories": 53},
        {"name": "Olives (10 medium)", "calories": 40},
        {"name": "Pickles (1 medium)", "calories": 12},
        {"name": "Radishes (1 cup)", "calories": 18},
        {"name": "Garbanzo Beans (1 cup cooked)", "calories": 269},
        {"name": "Apricot (1 medium)", "calories": 17},
        {"name": "Figs (1 medium)", "calories": 37},
        {"name": "Dates (1 medium)", "calories": 66},
        {"name": "Beets (1 cup)", "calories": 58},
        {"name": "Grapes (1 cup)", "calories": 62},
        {"name": "Kiwi (1 medium)", "calories": 42},
        {"name": "Strawberries (1 cup)", "calories": 49},
        {"name": "Cherry Tomatoes (1 cup)", "calories": 27},
        {"name": "Lettuce (1 cup)", "calories": 5},
        {"name": "Asparagus (1 cup)", "calories": 27},
        {"name": "Eggs Benedict", "calories": 370},
        {"name": "Chicken Caesar Salad", "calories": 470},
        {"name": "Smoothie (1 cup)", "calories": 130},
        {"name": "Espresso", "calories": 3},
        {"name": "Milk (1 cup)", "calories": 103},
        {"name": "Orange Juice (1 cup)", "calories": 112},
        {"name": "Coca-Cola (12 oz can)", "calories": 140},
        {"name": "Milkshake (12 oz)", "calories": 300},
        {"name": "Water (1 cup)", "calories": 0},
        {"name": "Coffee (1 cup)", "calories": 2},
        {"name": "Tea (1 cup)", "calories": 2},
        {"name": "Beer (12 oz)", "calories": 154},
        {"name": "Wine (5 oz)", "calories": 125},
        {"name": "Smoothie (1 cup)", "calories": 200},
        {"name": "Lemonade (1 cup)", "calories": 99},
        {"name": "Energy Drink (8 oz)", "calories": 110},
        {"name": "Sports Drink (12 oz)", "calories": 80}
    ]
    food_db_collection.insert_many(common_foods)
    
# User registration function
def register_user(username, password):
    if users_collection.find_one({"username": username}):
        return False, "Username already exists"
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = {"username": username, "password": hashed_password}
    users_collection.insert_one(user)
    return True, "User registered successfully"

# User login function
def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = users_collection.find_one({"username": username, "password": hashed_password})
    return user is not None

################# CRUD operations for meals ####################

# Function to add a meal entry
def add_meal(user_id, name, calories, date):
    meal = {"user_id": user_id, "name": name, "calories": calories, "date": date}
    result = meals_collection.insert_one(meal)
    return str(result.inserted_id)

# Function to retrieve meals for a user on a specific date
def get_meals(user_id, date):
    return list(meals_collection.find({"user_id": user_id, "date": date}))

# Function to update an existing meal entry
def update_meal(meal_id, name, calories):
    result = meals_collection.update_one(
        {"_id": ObjectId(meal_id)},
        {"$set": {"name": name, "calories": calories}}
    )
    return result.modified_count

# Function to delete a meal entry
def delete_meal(meal_id):
    result = meals_collection.delete_one({"_id": ObjectId(meal_id)})
    return result.deleted_count

# Function to calculate total calories consumed by a user on a specific date
def get_total_calories(user_id, date):
    meals = get_meals(user_id, date)
    return sum(meal['calories'] for meal in meals)

# Function to search the food database by name
def search_food_db(query):
    return list(food_db_collection.find({"name": {"$regex": query, "$options": "i"}}))

# KIVY Layouts and UI Components
class BackgroundColorBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos

# Login screen class
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical')
        
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        background_image = Image(source='background.jpeg', allow_stretch=False, keep_ratio=True)
        
        # Form layout for username and password inputs
        form_layout = BoxLayout(orientation='vertical', padding=[20, 20, 20, 50], spacing=10)
        
        # Welcome message at the top of the form
        welcome_message = Label(
            text='[color=#228B22]Welcome to our health tracking app![/color]\n[color=#4169E1]Please login/register to continue![/color]',
            size_hint_y=None, height=60, font_size=24,  # Increased font size
            halign='center',
            markup=True  # Enable markup for colored text
        )

        form_layout.add_widget(welcome_message)
        
        # Text inputs for username and password
        self.username_input = TextInput(hint_text='Username', size_hint_y=None, height=40)
        self.password_input = TextInput(hint_text='Password', password=True, size_hint_y=None, height=40)
        
        # Buttons for login and registration
        login_button = Button(
            text='Login', on_press=self.login, size_hint_y=None, height=50,  # Increased height for better appearance
            background_color=(0.2, 0.6, 0.8, 1), color=(1, 1, 1, 1),
            font_size=20  # Increased font size
        )
        register_button = Button(
            text='Register', on_press=self.register, size_hint_y=None, height=50,  # Increased height for better appearance
            background_color=(0.3, 0.7, 0.4, 1), color=(1, 1, 1, 1),
            font_size=20  # Increased font size
        )
        
        # Label for displaying messages (e.g., login errors)
        self.message_label = Label(text='', color=(1, 0, 0, 1), font_size=16)
        
        # Add widgets to the form layout
        form_layout.add_widget(self.username_input)
        form_layout.add_widget(self.password_input)
        form_layout.add_widget(login_button)
        form_layout.add_widget(register_button)
        form_layout.add_widget(self.message_label)
        
        # Add the background image and the form layout to the main layout
        main_layout.add_widget(background_image)
        main_layout.add_widget(form_layout)
        
        # Center the form layout on the screen
        form_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        
        # Add the main layout to the screen
        self.add_widget(main_layout)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    # Function to handle login button press
    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        if login_user(username, password):
            self.manager.current = 'main'
            self.manager.get_screen('main').user_id = username
        else:
            self.message_label.text = 'Invalid username or password'

    # Function to handle registration button press
    def register(self, instance):
        username = self.username_input.text
        password = self.username_input.text
        success, message = register_user(username, password)
        self.message_label.text = message

# Main screen class for main functionalities
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_id = None
        
        # Main layout with vertical orientation, padding, and spacing
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # White background using a canvas
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        # Update the background rectangle when the window is resized
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        # Create input fields for date, meal name, and calories
        self.date_input = TextInput(hint_text='Date (YYYY-MM-DD)', text=datetime.now().strftime('%Y-%m-%d'))
        self.meal_input = TextInput(hint_text='Meal Name')
        self.calories_input = TextInput(hint_text='Calories')
        
        # Create buttons for adding, viewing, and managing meals, and customize their appearance
        add_button = Button(
            text='Add Meal', on_press=self.add_meal,
            background_color=(0.2, 0.6, 0.8, 1), color=(1, 1, 1, 1), font_size=18
        )
        view_button = Button(
            text='View Meals', on_press=self.view_meals,
            background_color=(0.4, 0.8, 0.4, 1), color=(1, 1, 1, 1), font_size=18
        )
        total_button = Button(
            text='Get Total Calories', on_press=self.get_total,
            background_color=(0.6, 0.4, 0.8, 1), color=(1, 1, 1, 1), font_size=18
        )
        search_db_button = Button(
            text='Search Food Database', on_press=self.open_food_db_search,
            background_color=(0.8, 0.4, 0.2, 1), color=(1, 1, 1, 1), font_size=18
        )
        logout_button = Button(
            text='Logout', on_press=self.logout,
            background_color=(0.9, 0.1, 0.1, 1), color=(1, 1, 1, 1), font_size=18
        )
        
        # Label for displaying results
        self.result_label = Label(text='', color=(0, 0, 0, 1), font_size=16)
        
        # Add all widgets (input fields, buttons, label) to the main layout
        self.main_layout.add_widget(self.date_input)
        self.main_layout.add_widget(self.meal_input)
        self.main_layout.add_widget(self.calories_input)
        self.main_layout.add_widget(add_button)
        self.main_layout.add_widget(view_button)
        self.main_layout.add_widget(total_button)
        self.main_layout.add_widget(search_db_button)
        self.main_layout.add_widget(logout_button)
        self.main_layout.add_widget(self.result_label)
        
        # Meals layout with scrollable view
        self.meals_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.meals_layout.bind(minimum_height=self.meals_layout.setter('height'))
        
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 200))
        scroll_view.add_widget(self.meals_layout)
        self.main_layout.add_widget(scroll_view)
        
        # Add the main layout to the screen
        self.add_widget(self.main_layout)

    # Update the size and position of the background rectangle
    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    # Log out the user
    def logout(self, instance):
        # Reset the user ID
        self.user_id = None

        self.date_input.text = datetime.now().strftime('%Y-%m-%d') 
        self.meal_input.text = ''
        self.calories_input.text = ''
        self.meals_layout.clear_widgets()
        self.result_label.text = ''

        # Switch to the login screen
        self.manager.current = 'login'

    # Validate the input fields (date, meal name, calories)
    def validate_input(self, date, name, calories):
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return False, "Invalid date format. Use YYYY-MM-DD."
        
        if not name:
            return False, "Meal name cannot be empty."
        
        try:
            calories = int(calories)
            if calories <= 0:
                return False, "Calories must be a positive number."
        except ValueError:
            return False, "Calories must be a valid number."
        
        return True, None

    # Add a meal to the database
    def add_meal(self, instance):
        date = self.date_input.text
        name = self.meal_input.text
        calories = self.calories_input.text
        self.result_label.font_size = 24 

        # Validate input before adding the meal
        valid, message = self.validate_input(date, name, calories)
        if not valid:
            self.result_label.text = message
            return

        user_id = self.user_id  
        calories = int(calories)

        meal_id = add_meal(user_id, name, calories, date)
        self.result_label.text = f"Meal added successfully!"

        self.date_input.text = datetime.now().strftime('%Y-%m-%d')
        self.meal_input.text = ''
        self.calories_input.text = ''

    # View the meals for the selected date
    def view_meals(self, instance):
        self.meals_layout.clear_widgets()
        date = self.date_input.text
        self.result_label.font_size = 24 
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            self.result_label.text = "Invalid date format. Use YYYY-MM-DD."
            return
        
        meals = get_meals(self.user_id, date)
        if meals:
            for meal in meals:
                meal_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                meal_label = Label(text=f"{meal['name']} - {meal['calories']} calories", color=(0, 0, 0, 1))
                edit_button = Button(text='Edit', size_hint_x=None, width=60)
                edit_button.bind(on_press=lambda x, meal=meal: self.edit_meal(meal))
                delete_button = Button(text='Delete', size_hint_x=None, width=60)
                delete_button.bind(on_press=lambda x, id=meal['_id']: self.delete_meal(id))
                
                meal_layout.add_widget(meal_label)
                meal_layout.add_widget(edit_button)
                meal_layout.add_widget(delete_button)
                self.meals_layout.add_widget(meal_layout)
            
            self.result_label.text = f"Showing meals for {date}"
        else:
            self.result_label.text = 'No meals found for this date'

    # Edit a selected meal
    def edit_meal(self, meal):
        self.meal_input.text = meal['name']
        self.calories_input.text = str(meal['calories'])
        
        update_button = Button(
            text='Update Meal', on_press=lambda x: self.update_meal(meal['_id']),
            background_color=(0.5, 0.5, 1, 1), color=(1, 1, 1, 1), font_size=18
        )
        self.main_layout.add_widget(update_button)

    # Update the meal in the database
    def update_meal(self, meal_id):
        name = self.meal_input.text
        calories = self.calories_input.text
        
        is_valid, error_message = self.validate_input(self.date_input.text, name, calories)
        if not is_valid:
            self.result_label.text = error_message
            return
        
        update_meal(meal_id, name, int(calories))
        self.result_label.text = f'Updated meal with ID: {meal_id}'
        self.meal_input.text = ''
        self.calories_input.text = ''
        self.view_meals(None)
        self.main_layout.remove_widget(self.main_layout.children[0])

    # Delete a meal
    def delete_meal(self, meal_id):
        delete_meal(meal_id)
        self.result_label.text = f'Deleted meal with ID: {meal_id}'
        self.view_meals(None)

    # Get the total calories for a specific date
    def get_total(self, instance):
        self.result_label.text = ""

        date = self.date_input.text
        try:
            datetime.strptime(date, '%Y-%m-%d')
            total = get_total_calories(self.user_id, date)

            self.result_label.text = f'Total calories for {date}: {total}'
            self.result_label.font_size = 24

            # Provide feedback based on calorie count
            if total > 3000:
                self.result_label.text += "\nYou have reached the desired limit! Please cut back for better health."
            elif total < 1500:
                self.result_label.text += "\nYou need more calories. Increase your intake!"
    
        except ValueError:
            self.result_label.text = "Invalid date format. Use YYYY-MM-DD."


    # Open a food database search screen
    def open_food_db_search(self, instance):
        content = BoxLayout(orientation='vertical')
        self.search_input = TextInput(hint_text='Search for food', foreground_color=(0, 0, 0, 1))  # Black text
        search_button = Button(text='Search')
        search_button.bind(on_press=self.search_food_db)
        self.search_results = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.search_results.bind(minimum_height=self.search_results.setter('height'))
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 200))
        scroll_view.add_widget(self.search_results)
        content.add_widget(self.search_input)
        content.add_widget(search_button)
        content.add_widget(scroll_view)
        self.popup = Popup(title='Food Database Search', content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    # Search for food in the database
    def search_food_db(self, instance):
        query = self.search_input.text
        results = search_food_db(query)
        self.search_results.clear_widgets()
        for food in results:
            food_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            food_label = Label(text=f"{food['name']} - {food['calories']} calories", color=(1, 1, 1, 1))  # White text
            add_button = Button(text='Add', size_hint_x=None, width=60)
            add_button.bind(on_press=lambda x, f=food: self.add_food_from_db(f))
            food_layout.add_widget(food_label)
            food_layout.add_widget(add_button)
            self.search_results.add_widget(food_layout)

    # Add a food item from the search results to the meal input fields
    def add_food_from_db(self, food):
        self.meal_input.text = food['name']
        self.calories_input.text = str(food['calories'])
        self.popup.dismiss()
        self.add_meal(None)


# Popup for searching the food database
class FoodDBSearchPopup(Popup):
    def __init__(self, user_id, **kwargs):
        super().__init__(**kwargs)
        self.title = "Search Food Database"
        self.size_hint = (0.8, 0.8)

        layout = BackgroundColorBoxLayout(orientation='vertical', padding=10, spacing=10)

        self.search_input = TextInput(hint_text='Enter food name', size_hint_y=None, height=40, font_size=16)
        search_button = Button(text='Search', on_press=self.search_food_db, size_hint_y=None, height=50, background_color=(0.1, 0.5, 0.7, 1), color=(1, 1, 1, 1), font_size=16)
        self.results_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.results_layout.bind(minimum_height=self.results_layout.setter('height'))

        scroll_view = ScrollView(size_hint=(1, None), size=(400, 200))
        scroll_view.add_widget(self.results_layout)

        layout.add_widget(self.search_input)
        layout.add_widget(search_button)
        layout.add_widget(scroll_view)

        self.add_widget(layout)

    # Search the food database for matching items
    def search_food_db(self, instance):
        self.results_layout.clear_widgets()
        search_term = self.search_input.text.strip()

        if search_term:
            results = food_db_collection.find({"name": {"$regex": search_term, "$options": "i"}})
            for result in results:
                result_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                result_label = Label(text=f"{result['name']} ({result['calories']} calories)", font_size=16, color=(0.2, 0.2, 0.2, 1))
                result_layout.add_widget(result_label)
                self.results_layout.add_widget(result_layout)
                self.results_layout.add_widget(result_layout)
        else:
            result_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            result_label = Label(text="Please enter a valid search term.", font_size=16, color=(1, 1, 1, 1))
            result_layout.add_widget(result_label)
            self.results_layout.add_widget(result_layout)

# Screen Manager to handle screen transitions
class CalorieCounterApp(App):
    def build(self):
        
        # Create ScreenManager and set the transition effect
        sm = ScreenManager(transition=FadeTransition(duration=0.5))

        # Add your screens to the ScreenManager
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
 
        return sm

# Main entry point for the app
if __name__ == '__main__':
    CalorieCounterApp().run()

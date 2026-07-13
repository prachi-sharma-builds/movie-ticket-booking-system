import time

class Movie:
    def __init__(self, movie_name, ticket_price, movie_date, movie_venue):
        self.movie_name = movie_name
        self.ticket_price = ticket_price # Price of 1 movie ticket!
        self.movie_date = movie_date
        self.movie_venue = movie_venue
        print(" ")
        
    def movie_info(self):
        print("---Movie Information---")
        print(" ")
        print(f"Movie: {self.movie_name}")
        print(f"Movie Ticket Price is Rs.{self.ticket_price}/Seat")
        print(f"{self.movie_date}")
        print(f"{self.movie_venue}")
        
class MovieBooking(Movie):
    def __init__(self, movie_name, movie_date, movie_venue, ticket_price, customer_name):
        super().__init__(movie_name, ticket_price, movie_date, movie_venue)
        self.customer_name = customer_name
        self.seats = 0
        
    def book_seats(self, seatBooking,):
        self.seats = seatBooking
        currentCost = self.ticket_price*self.seats
        print(" ")
        print("---Your Booking and Price Details---\n")
        print(" ")
        print("Processing...")
        time.sleep(4)
        print(f"{self.seats} Seat(s) Booked Successfully!")
        print(f"Your Current Movie Cost: {currentCost}")
        print(" ")
        
    def extra_seats(self, extraBooking):
        self.seats = self.seats+extraBooking
        
        extraCost = self.ticket_price*extraBooking
        finalCurrentCost = self.ticket_price*self.seats
        print("---Your Final Booking and Pricing Details---")
        print(" ")
        print("Processing...")
        time.sleep(4)
        print(f"{extraBooking} Extra Seat(s) Booked Successfully!")
        print(f"Cost for Extra Seat(s) is Rs.{extraCost}")
        print(" ")
        print(f"Now Your Total Seat(s) are: {self.seats}")
        print(f"Cost for Total Seat(s) is Rs.{finalCurrentCost}")
        
        
        
    def customer_booking_info(self):
        ticket_cost = self.seats*self.ticket_price
        print("---Customer's Movie Booking Information---")
        print(" ")
        print(f"Selected Movie: {self.movie_name}")
        print(f"Movie Booked By {self.customer_name}")
        print(f"Total Seats Booked: {self.seats}")
        print(f"Total Cost of Ticket Price Including All The Seats: Rs.{ticket_cost}")
        

booking = MovieBooking("The Conjuring", "July 19, 2013", " Harrisville, Rhode Island", 300, "Prachi Sharma")
booking.movie_info()
booking.book_seats(6)
booking.extra_seats(2)
booking.customer_booking_info()

        
        
    
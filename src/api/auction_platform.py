"""
This is the API set to create a platform for auctioning items.
Any user can create an auctioning base to a limit of 3 platforms.
A platform is analogous to an auction site. 
The reason for different platforms is to allow for different auctioning rules and regulations.
The auctioning rules and regulations are set by the platform owner who creates the plaform.
"""
class AuctionPlatform():
    """
    An API class to do CRUD operations for the auction platform.
    We would need to create, update, delete and read the auction platform.
    """
    def __init__(self):
        """
        Initialize the class with the base class.
        """
        super().__init__()

    def create_auction_platform(self, platform_name, platform_owner, platform_owner_email, platform_owner_phone, platform_owner_address, platform_owner_city, platform_owner_country, platform_owner_zipcode, platform_owner_state, platform_owner_password):
        """
        Create an auction platform.
        """
        # Create a platform owner.
        platform_owner_id = self.create_user(platform_owner, platform_owner_email, platform_owner_phone, platform_owner_address, platform_owner_city, platform_owner_country, platform_owner_zipcode, platform_owner_state, platform_owner_password)
        # Create a platform.
        platform_id = self.create_platform(platform_name, platform_owner_id)
        # Return the platform id.
        return platform_id

    def update_auction_platform(self, platform_id, platform_name, platform_owner, platform_owner_email, platform_owner_phone, platform_owner_address, platform_owner_city, platform_owner_country, platform_owner_zipcode, platform_owner_state, platform_owner_password):
        """
        Update an auction platform.
        """
        # Update the platform owner.
        self.update_user(platform_owner, platform_owner_email, platform_owner_phone, platform_owner_address, platform_owner_city, platform_owner_country, platform_owner_zipcode, platform_owner_state, platform_owner_password)
        # Update the platform.
        self.update_platform(platform_id, platform_name)

    def delete_auction_platform(self, platform_id):
        """
        Delete an auction platform.
        """
        # Delete the platform.
        self.delete_platform(platform_id)

    def read_auction_platform(self, platform_id):
        """
        Read an auction platform.
        """
        # Read the platform.
        platform = self.read_platform(platform_id)
        # Return the platform.
        return platform
    

    
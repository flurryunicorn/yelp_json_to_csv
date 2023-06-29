BUSINESS = "business"
REVIEW = "review"
TIP = "tip"
CHECKIN = "checkin"
USER = "user"

def get_headers(_type):
    """
    Pre-defined headers for various categories
    """
    if _type == BUSINESS:
        return ["name", "city", "review_count", "hours", "categories", "latitude", \
                "stars", "attributes", "longitude", "address", "postal_code", "state", "is_open", \
                "business_id"]
    elif _type == REVIEW:
        return ["review_id", "user_id", "date", "useful", "text", "cool", "stars", "business_id", \
                "funny"]
    elif _type == TIP:
        return ["business_id", "user_id", "date", "text", "compliment_count"]
    elif _type == CHECKIN:
        return ["business_id", "date"]
    else:
        return ["user_id", "name", "review_count", "yelping_since", "friends", "useful", "funny", \
                "cool", "fans", "elite", "average_stars", "compliment_hot", "compliment_more", \
                "compliment_profile", "compliment_cute", "compliment_list", "compliment_note", \
                "compliment_plain", "compliment_cool", "compliment_funny", "compliment_writer", \
                "compliment_photos"]
    
def get_data(_type, _data):
    """
    Data-frame entries for various categories
    """
    data_arr = []
    for i in get_headers(_type):
        data_arr.append(_data['{}'.format(i)])
    
    return data_arr
from location_crud.models import Locations, Tags

def transform_error_payload(params):
    error_keys = ["geolocation-unsupported", 
                    "geolocation-fetch",
                    "geolocation-preview"] # Error keys defined in html
    errors = []
    for key in error_keys:
        if key in params:
            if key == "geolocation-unsupported":
                errors.append("Browser doesn't support geolocation functionality")
            elif key == "geolocation-fetch":
                errors.append("Failed while fetching the geolocation")
            elif key == "geolocation-preview":
                errors.append("Failed while redirecting to link")
            else:
                errors.append("Faield while performing action")
    return errors

def create_location_and_tags(**data):
    try:
        location = Locations(
                    name=data["name"], 
                    link=data["link"], 
                    city=data.get("city", ""),
                    user_id=data["user"])
        location.save()
        tags = data.get("hidden_tags", "").strip()
        if tags:
            for tag in tags.split(","):
                Tags(name=tag, user_id=data["user"], location_id=location).save()
        return "Location added successfully.", None
    except Exception as e:
        return None, "Location creation failed."

def transform_tag_data(tags_data):
    tags_string = ""
    for tag_index in range(0, len(tags_data)):
        tags_string += tags_data[tag_index].name
        if tag_index != len(tags_data)-1:
            tags_string += ","
    return tags_string

def update_location_and_tags(**data):
    try:
        location = Locations.objects.get(id=data["location_id"])
        tags = Tags.objects.filter(location_id=data["location_id"]).all()
        updated_keys = []

        LOCATION_KEYS = ["name", "link", "city"]

        for key in LOCATION_KEYS:
            if key in data and data[key] != getattr(location, key):
                updated_keys.append(key)

        if len(updated_keys) != 0:
            location.save(update_fields=updated_keys)

        if len(tags) == 0 and len(data["hidden_tags"]) > 0:
            new_tags = data["hidden_tags"].split(",")
            for tag in new_tags:
                Tags(name=tag, location_id=location, user_id=data["user"]).save()
        elif len(tags) > 0 and len(data["hidden_tags"]) == 0:
            for tag in tags:
                tag.delete()
        elif len(tags) > 0 and len(data["hidden_tags"]) > 0:
            tags_dict = {"old": {}, "new": {}}

            # Form list of tags will be stored in new key
            for tag in data["hidden_tags"].split(","):
                tags_dict["new"][tag] = None
            
            # DB list of tags will be stored in old key
            for tag in tags:
                tags_dict["old"][tag.name] = tag
            
            # If any db tag not in form tag then remove the db tag
            for tag in tags_dict["old"]:
                if tag not in tags_dict["new"]:
                    tags_dict["old"][tag].delete()

            # if any form tag is not in db tag then add the form tag
            for tag in tags_dict["new"]:
                if tag not in tags_dict["old"]:
                    Tags(name=tag, location_id=location, user_id=data["user"]).save()
        else:
            print("No tag update required")

        return "Location updated successfully.", None
    
    except Exception as e:
        print(e)
        return None, "Location update failed."

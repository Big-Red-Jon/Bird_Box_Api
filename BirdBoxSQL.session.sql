select *
from birdbox_sighting;
select *
from auth_user;
select *
from birdbox_sighting;
select *
from birdbox_sighting
    Inner Join birdbox_location
Where birdbox_sighting.location_id = birdbox_location.id;
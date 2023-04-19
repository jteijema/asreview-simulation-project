import sys
import exoscale
from pathlib import Path


def upload_simulation_to_storage(simulation_file, simulation_id, bucket):
    simulation_id = simulation_id.replace(" ", "_")
    filepath = Path(simulation_file)
    print(f"Uploading {simulation_file} to sos://{bucket}/{simulation_id}/{filepath.name}")   
    exo = exoscale.Exoscale()
    bucket = exo.storage.get_bucket(bucket)
    storage_location = f"simulations/{simulation_id}/{filepath.name}"
    bucket.put_file(src=simulation_file, dst=storage_location, acl="public-read")

upload_simulation_to_storage(sys.argv[1], sys.argv[2], sys.argv[3])

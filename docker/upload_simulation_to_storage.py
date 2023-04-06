import sys
import exoscale


def upload_simulation_to_storage(simulation_file, simulation_id, bucket):
    print(f"Uploading {simulation_file} to sos://{bucket}/{simulation_id}/")   
    exo = exoscale.Exoscale()
    bucket = exo.storage.get_bucket(bucket)
    storage_location = f"simulations/{simulation_id}/{simulation_file}"
    bucket.put_file(src=simulation_file, dst=storage_location, acl="public-read")

upload_simulation_to_storage(sys.argv[1], sys.argv[2], sys.argv[3])
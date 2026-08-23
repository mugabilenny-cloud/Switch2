from services.supabase import get_supabase
from services.device import get_device_token


def get_ads(limit=3):

    supabase = get_supabase()

    device_token = get_device_token()

    result = supabase.rpc(
        "fn_get_ads_for_device",
        {
            "p_device_token": device_token,
            "p_limit": limit
        }
    ).execute()

    return result.data or []


def record_impression(ad_id):

    supabase = get_supabase()

    device_token = get_device_token()

    return supabase.rpc(
        "fn_record_ad_impression",
        {
            "p_ad_id": ad_id,
            "p_device_token": device_token
        }
    ).execute()


def record_click(ad_id):

    supabase = get_supabase()

    device_token = get_device_token()

    return supabase.rpc(
        "fn_record_ad_click",
        {
            "p_ad_id": ad_id,
            "p_device_token": device_token
        }
    ).execute()

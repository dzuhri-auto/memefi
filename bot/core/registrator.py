from bot.utils import logger
from helpers import get_tele_user_obj_from_query_id


async def register_query_id() -> None:

    add = True
    while add:
        query_id_str = input("\nMasukkan query id (press Enter to exit): ")

        if not query_id_str:
            break
        
        tele_user_obj = get_tele_user_obj_from_query_id(query_id_str)
        username = tele_user_obj.get("username")
        first_name = tele_user_obj.get("first_name")
        last_name = tele_user_obj.get("last_name")
        
        username_exist = False
        
        with open("query_ids.txt", "r+") as fd:
            content = fd.readlines()
            if content:
                existing_username = []
                for cnt in content:
                    cnt_user_obj = get_tele_user_obj_from_query_id(cnt)
                    cnt_username = cnt_user_obj.get("username")
                    existing_username.append(cnt_username)

                if username in set(existing_username):
                    username_exist = True
                else:
                    fd.write(f"\n{query_id_str}")
            else:
                fd.write(f"{query_id_str.strip()}")

        if username_exist:
            logger.error(f"Akun @{username} sudah terdaftar, tambah akun yg lainnya aja gan !")
        else:
            logger.success(f"Akun @{username} | {first_name} {last_name} | berhasil ditambahkan !")

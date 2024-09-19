from Wealth_App.configs.global_configs import (
    selected_environment,
    environment_global_configs,
)


class Apis_End_point:
    default_endpoint = environment_global_configs.get(selected_environment).get(
        "defaultEndPoint")

    # ************************* MasterData *******************************

    # ------------------------AddressType Controller------------------------
    FETCH_ADDRESS_TYPES = (
        default_endpoint + f"MasterData/AddressType/fetchAddressTypes?limit=%s&offset=%s"
    )

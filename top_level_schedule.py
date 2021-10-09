from helper import iso_date_to_datetime, datetime_to_timestamp

TOP_LEVEL_SCHEDULE = {
    ###########################################################
    # 12,600,000 MTA to be emitted until next emission drop.  #
    ###########################################################
    "2021-04-05": {
        "MTA/WETH": 28_750,
        "staking": 40_000,
        "pools": 173_077 - 28_750 - 40_000,
    },
    "2021-04-12": {
        "MTA/WETH": 28_750,
        "staking": 40_000,
        "pools": 173_077 - 28_750 - 40_000,
    },
    "2021-04-19": {
        "MTA/WETH": 25781,
        "staking": 40_000,
        "pools": 207_692 - 25871 - 40_000,
    },
    "2021-04-26": {
        "MTA/WETH": 22812,
        "staking": 40_000,
        "pools": 207_692 - 22812 - 40_000,
    },
    "2021-05-03": {
        "MTA/WETH": 19843,
        "staking": 40_000,
        "pools": 207_692 - 19843 - 40_000,
    },
    "2021-05-10": {
        "MTA/WETH": 16875,
        "staking": 40_000,
        "pools": 207_692 - 16875 - 40_000,
    },
    "2021-05-17": {
        "MTA/WETH": 13906,
        "staking": 40_000,
        "pools": 242_308 - 13906 - 40_000,
    },
    "2021-05-24": {
        "MTA/WETH": 10937,
        "staking": 40_000,
        "pools": 242_308 - 10937 - 40_000,
    },
    "2021-05-31": {
        "MTA/WETH": 7968,
        "staking": 40_000,
        "pools": 242_308 - 7968 - 40_000,
    },
    "2021-06-07": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 242_308 - 5000 - 40_000,
    },
    "2021-06-14": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 242_308 - 5000 - 40_000,
    },
    "2021-06-21": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 242_308 - 5000 - 40_000,
    },
    "2021-06-28": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 276_923 - 5000 - 40_000,
    },
    "2021-07-05": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 276_923 - 5000 - 40_000,
    },
    "2021-07-12": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 20_832,
        "p-MTA": 15_000,
        "pools": 276_923 - 5000 - 40_000 - 20_832 - 15_000,
    },
    ## MCCP-8 Starts: 1
    "2021-07-19": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 20_832,
        "p-MTA": 15_000,
        "pools": 242_308 - 5000 - 40_000 - 20_832 - 15_000,
    },
    "2021-07-26": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 20_832,
        "p-MTA": 15_000,
        "p-frax": 0,
        "pools": 242_308 - 5000 - 40_000 - 20_832 - 15_000,
    },
    "2021-08-02": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 20_832,
        "p-MTA": 15_000,
        "p-frax": 0,
        "pools": 242_308 - 5000 - 40_000 - 20_832 - 15_000,
    },
    "2021-08-09": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 20_832,
        "p-MTA": 15_000,
        "p-frax": 0,
        "pools": 242_308 - 5000 - 40_000 - 20_832 - 15_000,
    },
    "2021-08-16": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 20_832,
        "p-MTA": 15_000,
        "p-frax": 10_000,
        "pools": 242_308 - 5000 - 40_000 - 20_832 - 15_000 - 10_000,
    },
    "2021-08-23": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 17_360, # 6 weeks in, 6 weeks remaining. Previous week double spend, reduce proportionately
        "p-MTA": 15_000,
        "p-frax": 10_000,
        "pools": 238_836 - 5000 - 40_000 - 17_360 - 15_000 - 10_000,
    },
    ## MCCP-8 Finishes here
    ## PDP 28: Reward distribution for weeks 35-41
    "2021-08-30": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 17_360,
        "p-MTA": 15_000,
        "p-frax": 10_000,
        "pools": 207_692 - 5000 - 40_000 - 17_360 - 15_000 - 10_000,
    },
    "2021-09-06": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 17_360,
        "p-MTA": 15_000,
        "p-frax": 10_000,
        "pools": 207_692 - 5000 - 40_000 - 17_360 - 15_000 - 10_000,
    },
    "2021-09-13": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "p-imUSD": 17_360,
        "p-MTA": 15_000,
        "p-frax": 10_000,
        "pools": 207_692 - 5000 - 40_000 - 17_360 - 15_000 - 10_000,
    },
    "2021-09-20": {
        "MTA/WETH": 5000,
        "staking-v2-mta": 25_540,
        "staking-v2-bpt": 15_720,
        "p-imUSD": 17_360,
        "p-MTA": 15_000,
        "p-frax": 10_000,
        "pools": 207_692 - 5000 - 25_540 - 15_720 - 17_360 - 15_000 - 10_000,
    },
    "2021-09-27": {
        "MTA/WETH": 5000,
        "staking-v2-mta": 32_500,
        "staking-v2-bpt": 20_000,
        "p-imUSD": 17_360,
        "p-MTA": 15_000,
        "p-frax": 10_000,
        "pools": 207_692 - 5000 - 32_500 - 20_000 - 17_360 - 15_000 - 10_000,
    },
    "2021-10-04": {
        "MTA/WETH": 5000,
        "staking-v2-mta": 32_500,
        "staking-v2-bpt": 20_000,
        "p-imUSD": 17_360,
        "p-MTA": 15_000,
        "p-frax": 10_000,
        "pools": 207_692 - 5000 - 32_500 - 20_000 - 17_360 - 15_000 - 10_000,
    },
    ## PDP 28: FINISHES HERE
    "2021-10-11": {
        "MTA/WETH": 5000,
        "staking-v2-mta": 32_500,
        "staking-v2-bpt": 20_000,
        "p-imUSD": 17_360,
        "p-MTA": 15_000,
        "p-frax": 10_000,
        "pools": 207_692 - 5000 - 32_500 - 20_000 - 17_360 - 15_000 - 10_000,
    },
    "2021-10-18": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-10-25": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-11-01": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-11-08": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-11-15": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-11-22": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-11-29": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-12-06": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-12-13": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-12-20": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2021-12-27": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2022-01-03": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2022-01-10": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2022-01-17": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2022-01-24": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2022-01-31": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 237_500 - 5000 - 40_000,
    },
    "2022-02-07": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 224_128 - 5000 - 40_000,
    },
    "2022-02-14": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 212_500 - 5000 - 40_000,
    },
    "2022-02-21": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 212_500 - 5000 - 40_000,
    },
    "2022-02-28": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 212_500 - 5000 - 40_000,
    },
    "2022-03-07": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 212_500 - 5000 - 40_000,
    },
    "2022-03-14": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 212_500 - 5000 - 40_000,
    },
    "2022-03-21": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 212_500 - 5000 - 40_000,
    },
    "2022-03-28": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 212_500 - 5000 - 40_000,
    },
    ##############################################################
    # EMISSION DROP                                              #
    # 10,500,000 MTA to be emitted until the next emission drop. #
    ##############################################################
    "2022-04-04": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201927 - 5000 - 40_000,
    },
    "2022-04-11": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-04-18": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-04-25": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-05-02": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-05-09": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-05-16": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-05-23": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-05-30": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-06-06": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-06-13": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-06-20": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-06-27": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-07-04": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-07-11": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-07-18": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-07-25": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-08-01": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-08-08": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-08-15": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-08-22": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-08-29": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-09-05": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-09-12": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-09-19": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-09-26": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-10-03": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-10-10": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-10-17": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-10-24": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-10-31": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-11-07": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-11-14": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-11-21": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-11-28": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-12-05": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-12-12": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-12-19": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2022-12-26": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-01-02": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-01-09": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-01-16": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-01-23": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-01-30": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-02-06": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-02-13": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-02-20": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-02-27": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-03-06": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-03-13": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-03-20": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    "2023-03-27": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 201923 - 5000 - 40_000,
    },
    ##############################################################
    # EMISSION DROP                                              #
    # 8,400,000 MTA to be emitted until the next emission drop.  #
    ##############################################################
    "2023-04-03": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161562 - 5000 - 40_000,
    },
    "2023-04-10": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-04-17": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-04-24": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-05-01": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-05-08": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-05-15": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-05-22": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-05-29": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-06-05": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-06-12": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-06-19": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-06-26": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-07-03": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-07-10": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-07-17": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-07-24": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-07-31": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-08-07": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-08-14": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-08-21": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-08-28": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-09-04": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-09-11": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-09-18": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-09-25": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-10-02": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-10-09": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-10-16": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-10-23": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-10-30": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-11-06": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-11-13": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-11-20": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-11-27": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-12-04": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-12-11": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-12-18": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2023-12-25": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-01-01": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-01-08": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-01-15": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-01-22": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-01-29": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-02-05": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-02-12": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-02-19": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-02-26": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-03-04": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-03-11": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-03-18": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    "2024-03-25": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 161538 - 5000 - 40_000,
    },
    ##############################################################
    # EMISSION DROP                                              #
    # 6,300,000 MTA to be emitted until the next emission drop.  #
    ##############################################################
    "2024-04-01": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121175 - 5000 - 40_000,
    },
    "2024-04-08": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121175 - 5000 - 40_000,
    },
    "2024-04-15": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-04-22": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-04-29": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-05-06": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-05-13": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-05-20": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-05-27": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-06-03": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-06-10": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-06-17": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-06-24": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-07-01": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-07-08": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-07-15": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-07-22": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-07-29": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-08-05": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-08-12": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-08-19": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-08-26": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-09-02": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-09-09": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-09-16": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-09-23": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-09-30": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-10-07": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-10-14": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-10-21": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-10-28": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-11-04": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-11-11": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-11-18": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-11-25": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-12-02": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-12-09": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-12-16": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-12-23": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2024-12-30": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-01-06": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-01-13": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-01-20": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-01-27": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-02-03": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-02-10": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-02-17": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-02-24": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-03-03": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-03-10": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-03-17": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    "2025-03-24": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 121153 - 5000 - 40_000,
    },
    ##############################################################
    # EMISSION DROP                                              #
    # 3,360,000 MTA to be emitted until the next emission drop.  #
    ##############################################################
    "2025-03-31": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64635 - 5000 - 40_000,
    },
    "2025-04-07": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-04-14": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-04-21": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-04-28": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-05-05": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-05-12": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-05-19": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-05-26": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-06-02": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-06-09": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-06-16": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-06-23": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-06-30": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-07-07": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-07-14": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-07-21": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-07-28": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-08-04": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-08-11": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-08-18": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-08-25": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-09-01": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-09-08": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-09-15": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-09-22": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-09-29": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-10-06": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-10-13": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-10-20": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-10-27": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-11-03": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-11-10": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-11-17": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-11-24": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-12-01": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-12-08": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-12-15": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-12-22": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2025-12-29": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-01-05": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-01-12": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-01-19": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-01-26": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-02-02": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-02-09": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-02-16": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-02-23": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-03-02": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-03-09": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-03-16": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
    "2026-03-23": {
        "MTA/WETH": 5000,
        "staking": 40_000,
        "pools": 64615 - 5000 - 40_000,
    },
}


def test_total_emission():
    total_emission = sum([sum(list(i.values())) for i in TOP_LEVEL_SCHEDULE.values()])

    # assert abs(total_emission - 42_000_000) <= 1.

    top_level_arr = list(TOP_LEVEL_SCHEDULE.items())
    top_level_arr = sorted(top_level_arr, key=lambda x: x[0])

    year1 = sum([sum(i[1].values()) for i in top_level_arr[:52]])
    year2 = sum([sum(i[1].values()) for i in top_level_arr[52 : 2 * 52]])
    year3 = sum([sum(i[1].values()) for i in top_level_arr[2 * 52 : 3 * 52]])
    year4 = sum([sum(i[1].values()) for i in top_level_arr[3 * 52 : 4 * 52]])
    year5 = sum([sum(i[1].values()) for i in top_level_arr[4 * 52 : 5 * 52]])

    print("# weeks:", len(TOP_LEVEL_SCHEDULE))
    print("Total emission:", total_emission)
    print("Year 1: %d MTA" % (year1))
    print("Year 2: %d MTA" % (year2))
    print("Year 3: %d MTA" % (year3))
    print("Year 4: %d MTA" % (year4))
    print("Year 5: %d MTA" % (year5))

    assert abs(year1 - 12_600_000) <= 1.0
    assert abs(year2 - 10_500_000) <= 1.0
    assert abs(year3 - 8_400_000) <= 1.0
    assert abs(year4 - 6_300_000) <= 1.0
    assert abs(year5 - 3_360_000) <= 1.0

def get_most_recent_date(input_dt, offset):
    top_level_arr = list(TOP_LEVEL_SCHEDULE.keys())
    top_level_arr = sorted(top_level_arr, key=lambda x: x[0])

    input_ts = datetime_to_timestamp(input_dt)

    for date in reversed(top_level_arr):
        ts = datetime_to_timestamp(iso_date_to_datetime(date))
        if input_ts + offset >= ts:
            return date

    return False


if __name__ == "__main__":
    test_total_emission()

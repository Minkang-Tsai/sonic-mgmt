MINIMUM_TABLE= {
    'x86_64-mlnx_msn2700-r0': {
        "unk_trust":   {"-127:20":13, "21:25":14 , "26:30":15, "31:120":16},
        "unk_untrust": {"-127:20":13, "21:25":14 , "26:30":15, "31:120":16}
    },
    'x86_64-mlnx_msn2740-r0': {
        "unk_trust":   {"-127:120":13},
        "unk_untrust": {"-127:15":13, "16:30":14 , "31:35":15, "36:120":17},
    },
    'x86_64-mlnx_msn2410-r0': {
        "unk_trust":   {"-127:20":13, "21:25":14 , "26:30":15, "31:120":16},
        "unk_untrust": {"-127:20":13, "21:25":14 , "26:30":15, "31:120":16}
    },
    'x86_64-mlnx_msn2100-r0': {
        "unk_trust":   {"-127:40":12, "41:120":13},
        "unk_untrust": {"-127:15":12, "16:25":13, "26:30":14, "31:35":15, "36:120":16}
    },
    'x86_64-mlnx_msn2010-r0': {
        "unk_trust":   {"-127:120":12},
        "unk_untrust": {"-127:15":12, "16:20":13 , "21:30":14, "31:35":15, "36:120":16}
    },
    'x86_64-mlnx_msn3700-r0': {
        "unk_trust":   {"-127:25":12, "26:40":13 , "41:120":14},
        "unk_untrust": {"-127:15":12, "16:30":13 , "31:35":14, "36:40":15, "41:120":16},
    },
    'x86_64-mlnx_msn3800-r0': {
        "unk_trust":   {"-127:30":12, "31:40":13 , "41:120":14},
        "unk_untrust": {"-127:0":12, "1:10":13 , "11:15":14, "16:20":15, "21:35":16, "36:120":17},
    },
    'x86_64-mlnx_msn4700-r0': {
        "unk_trust":   {"-127:35":14, "36:120":15},
        "unk_untrust": {"-127:35":14, "36:120":15},
    },
    'x86_64-mlnx_msn3420-r0': {
        "unk_trust":   {"-127:120":12},
        "unk_untrust": {"-127:25":12, "26:35":13, "36:40":14, "41:120":16},
    },
    'x86_64-mlnx_msn4600c-r0': {
        "unk_trust":   {"-127:40":12, "41:120":13},
        "unk_untrust": {"-127:5":12, "6:20":13, "21:30":14, "31:35":15, "36:40":16, "41:120":17},
    }
}


def get_min_table(dut):
    """
    Get the dynamic minimum fan speed table for the given switch dut object
    :param dut: switch dut object
    :return: A dictionary contains the dynamic minimum fan speed data
    """
    dut_platform = dut.facts["platform"]
    return MINIMUM_TABLE[dut_platform]

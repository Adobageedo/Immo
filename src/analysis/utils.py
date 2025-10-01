def merge_dvf_melo(dvf_df, melo_df, group_field="code_insee"):
    """
    Merge les données DVF et Melo pour avoir comparaison prix/m²
    """
    merged = melo_df.merge(
        dvf_df, on=group_field, how="left", suffixes=("_melo", "_dvf")
    )
    return merged

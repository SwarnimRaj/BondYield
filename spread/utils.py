def clean_data(df):
    df['type'] = df['type'].str.strip()
    df['term'] = df['term'].str.rstrip(' years').astype(float)
    df['yield'] = df['yield'].str.rstrip('%').astype(float)
    corp_bonds = df[df['type'] == 'corporate']
    govt_bonds = df[df['type'] == 'government']
    return corp_bonds, govt_bonds

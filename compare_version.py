def compare(v1, v2):
    try:
        v1, v2 = float(v1), float(v2)
        if v1 > v2:
            return 'version {} is greater than version {}'.format(v1, v2)
        elif v1 < v2:
            return 'version {} is less than version {}'.format(v1, v2)
        else:
            return 'version {} is equal to version {}'.format(v1, v2)
    except ValueError:
        return 'Please give valid version number'

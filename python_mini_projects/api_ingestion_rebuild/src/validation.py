


def validation_schema(datas):
    # 1. Check empty list
    if not datas:
        raise ValueError("Validation failed: input data is empty and cannot be loaded into database")

    # 2. Validate each record
    for data in datas:
        # Check key existence first
        if 'id' not in data:
            raise ValueError("Validation failed: missing primary key 'id' in record")

        if data['id'] is None:
            raise ValueError("Validation failed: primary key 'id' is null")

        if 'email' not in data:
            raise ValueError("Validation failed: missing required field 'email' in record")

        if not data['email']:
            raise ValueError("Validation failed: 'email' value is empty")

    # 3. Return unchanged data if all checks pass
    return datas
   
      

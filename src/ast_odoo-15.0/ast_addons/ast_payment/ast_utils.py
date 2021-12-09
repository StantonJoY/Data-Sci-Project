Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='consteq', asname=None),
                alias(name='float_round', asname=None),
                alias(name='ustr', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='hmac', asname='hmac_tool')],
            level=0,
        ),
        FunctionDef(
            name='generate_access_token',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='values', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Generate an access token based on the provided values.\n\n    The token allows to later verify the validity of a request, based on a given set of values.\n    These will generally include the partner id, amount, currency id, transaction id or transaction\n    reference.\n    All values must be convertible to a string.\n\n    :param list values: The values to use for the generation of the token\n    :return: The generated access token\n    :rtype: str\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='token_str', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='|', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            GeneratorExp(
                                elt=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[Name(id='val', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='val', ctx=Store()),
                                        iter=Name(id='values', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='access_token', ctx=Store())],
                    value=Call(
                        func=Name(id='hmac_tool', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='su',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            Constant(value='generate_access_token', kind=None),
                            Name(id='token_str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='access_token', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='check_access_token',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='access_token', annotation=None, type_comment=None)],
                vararg=arg(arg='values', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Check the validity of the access token for the provided values.\n\n    The values must be provided in the exact same order as they were to `generate_access_token`.\n    All values must be convertible to a string.\n\n    :param str access_token: The access token used to verify the provided values\n    :param list values: The values to verify against the token\n    :return: True if the check is successful\n    :rtype: bool\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='authentic_token', ctx=Store())],
                    value=Call(
                        func=Name(id='generate_access_token', ctx=Load()),
                        args=[
                            Starred(
                                value=Name(id='values', ctx=Load()),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BoolOp(
                        op=And(),
                        values=[
                            Name(id='access_token', ctx=Load()),
                            Call(
                                func=Name(id='consteq', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='ustr', ctx=Load()),
                                        args=[Name(id='access_token', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='authentic_token', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='singularize_reference_prefix',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='prefix', annotation=None, type_comment=None),
                    arg(arg='separator', annotation=None, type_comment=None),
                    arg(arg='max_length', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='tx', kind=None),
                    Constant(value='-', kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Make the prefix more unique by suffixing it with the current datetime.\n\n    When the prefix is a placeholder that would be part of a large sequence of references sharing\n    the same prefix, such as "tx" or "validation", singularizing it allows to make it part of a\n    single-element sequence of transactions. The computation of the full reference will then execute\n    faster by failing to find existing references with a matching prefix.\n\n    If the `max_length` argument is passed, the end of the prefix can be stripped before\n    singularizing to ensure that the result accounts for no more than `max_length` characters.\n\n    :param str prefix: The custom prefix to singularize\n    :param str separator: The custom separator used to separate the prefix from the suffix\n    :param int max_length: The maximum length of the singularized prefix\n    :return: The singularized prefix\n    :rtype: str\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='prefix', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='prefix', ctx=Store())],
                            value=Constant(value='tx', kind=None),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Name(id='max_length', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='DATETIME_LENGTH', ctx=Store())],
                            value=Constant(value=14, kind=None),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='max_length', ctx=Load()),
                                ops=[GtE()],
                                comparators=[
                                    BinOp(
                                        left=BinOp(
                                            left=Constant(value=1, kind=None),
                                            op=Add(),
                                            right=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='separator', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Name(id='DATETIME_LENGTH', ctx=Load()),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='prefix', ctx=Store())],
                            value=Subscript(
                                value=Name(id='prefix', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=BinOp(
                                        left=BinOp(
                                            left=Name(id='max_length', ctx=Load()),
                                            op=Sub(),
                                            right=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='separator', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Sub(),
                                        right=Name(id='DATETIME_LENGTH', ctx=Load()),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=JoinedStr(
                        values=[
                            FormattedValue(
                                value=Name(id='prefix', ctx=Load()),
                                conversion=-1,
                                format_spec=None,
                            ),
                            FormattedValue(
                                value=Name(id='separator', ctx=Load()),
                                conversion=-1,
                                format_spec=None,
                            ),
                            FormattedValue(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='Datetime',
                                                    ctx=Load(),
                                                ),
                                                attr='now',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='strftime',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='%Y%m%d%H%M%S', kind=None)],
                                    keywords=[],
                                ),
                                conversion=-1,
                                format_spec=None,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='to_major_currency_units',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='minor_amount', annotation=None, type_comment=None),
                    arg(arg='currency', annotation=None, type_comment=None),
                    arg(arg='arbitrary_decimal_number', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return the amount converted to the major units of its currency.\n\n    The conversion is done by dividing the amount by 10^k where k is the number of decimals of the\n    currency as per the ISO 4217 norm.\n    To force a different number of decimals, set it as the value of the `decimal_number` argument.\n\n    :param float minor_amount: The amount in minor units, to convert in major units\n    :param recordset currency: The currency of the amount, as a `res.currency` record\n    :param int arbitrary_decimal_number: The number of decimals to use instead of that of ISO 4217\n    :return: The amount in major units of its currency\n    :rtype: int\n    ', kind=None),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='currency', ctx=Load()),
                            attr='ensure_one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                If(
                    test=Compare(
                        left=Name(id='arbitrary_decimal_number', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='decimal_number', ctx=Store())],
                            value=Attribute(
                                value=Name(id='currency', ctx=Load()),
                                attr='decimal_places',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='decimal_number', ctx=Store())],
                            value=Name(id='arbitrary_decimal_number', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                ),
                Return(
                    value=BinOp(
                        left=Call(
                            func=Name(id='float_round', ctx=Load()),
                            args=[
                                Name(id='minor_amount', ctx=Load()),
                                Constant(value=0, kind=None),
                            ],
                            keywords=[],
                        ),
                        op=Div(),
                        right=BinOp(
                            left=Constant(value=10, kind=None),
                            op=Pow(),
                            right=Name(id='decimal_number', ctx=Load()),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='to_minor_currency_units',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='major_amount', annotation=None, type_comment=None),
                    arg(arg='currency', annotation=None, type_comment=None),
                    arg(arg='arbitrary_decimal_number', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return the amount converted to the minor units of its currency.\n\n    The conversion is done by multiplying the amount by 10^k where k is the number of decimals of\n    the currency as per the ISO 4217 norm.\n    To force a different number of decimals, set it as the value of the `decimal_number` argument.\n\n    Note: currency.ensure_one() if arbitrary_decimal_number is not provided\n\n    :param float major_amount: The amount in major units, to convert in minor units\n    :param recordset currency: The currency of the amount, as a `res.currency` record\n    :param int arbitrary_decimal_number: The number of decimals to use instead of that of ISO 4217\n    :return: The amount in minor units of its currency\n    :rtype: int\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='arbitrary_decimal_number', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='decimal_number', ctx=Store())],
                            value=Name(id='arbitrary_decimal_number', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='currency', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='decimal_number', ctx=Store())],
                            value=Attribute(
                                value=Name(id='currency', ctx=Load()),
                                attr='decimal_places',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                Return(
                    value=Call(
                        func=Name(id='int', ctx=Load()),
                        args=[
                            BinOp(
                                left=Call(
                                    func=Name(id='float_round', ctx=Load()),
                                    args=[
                                        Name(id='major_amount', ctx=Load()),
                                        Name(id='decimal_number', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                op=Mult(),
                                right=BinOp(
                                    left=Constant(value=10, kind=None),
                                    op=Pow(),
                                    right=Name(id='decimal_number', ctx=Load()),
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='build_token_name',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='payment_details_short', annotation=None, type_comment=None),
                    arg(arg='final_length', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=16, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=" Pad plain payment details with leading X's to build a token name of the desired length.\n\n    :param str payment_details_short: The plain part of the payment details (usually last 4 digits)\n    :param int final_length: The desired final length of the token name (16 for a bank card)\n    :return: The padded token name\n    :rtype: str\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='payment_details_short', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='payment_details_short', ctx=Load()),
                            Constant(value='????', kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=JoinedStr(
                        values=[
                            FormattedValue(
                                value=BinOp(
                                    left=Constant(value='X', kind=None),
                                    op=Mult(),
                                    right=BinOp(
                                        left=Name(id='final_length', ctx=Load()),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='payment_details_short', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                                conversion=-1,
                                format_spec=None,
                            ),
                            FormattedValue(
                                value=Name(id='payment_details_short', ctx=Load()),
                                conversion=-1,
                                format_spec=None,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='format_partner_address',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='address1', annotation=None, type_comment=None),
                    arg(arg='address2', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='', kind=None),
                    Constant(value='', kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Format a two-parts partner address into a one-line address string.\n\n    :param str address1: The first part of the address, usually the `street1` field\n    :param str address2: The second part of the address, usually the `street2` field\n    :return: The formatted one-line address\n    :rtype: str\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='address1', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='address1', ctx=Load()),
                            Constant(value='', kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='address2', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='address2', ctx=Load()),
                            Constant(value='', kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=JoinedStr(
                                values=[
                                    FormattedValue(
                                        value=Name(id='address1', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' ', kind=None),
                                    FormattedValue(
                                        value=Name(id='address2', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                ],
                            ),
                            attr='strip',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='split_partner_name',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='partner_name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Split a single-line partner name in a tuple of first name, last name.\n\n    :param str partner_name: The partner name\n    :return: The splitted first name and last name\n    :rtype: tuple\n    ', kind=None),
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='partner_name', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='partner_name', ctx=Load()),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_customer_ip_address',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Return(
                    value=BoolOp(
                        op=Or(),
                        values=[
                            BoolOp(
                                op=And(),
                                values=[
                                    Name(id='request', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='remote_addr',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            Constant(value='', kind=None),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)

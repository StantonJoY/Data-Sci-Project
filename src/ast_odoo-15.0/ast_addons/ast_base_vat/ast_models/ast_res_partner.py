Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='string', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='stdnum', asname=None)],
        ),
        ImportFrom(
            module='stdnum.eu.vat',
            names=[alias(name='check_vies', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='stdnum.exceptions',
            names=[alias(name='InvalidComponent', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='stdnum.util',
            names=[alias(name='clean', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='ustr', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_eu_country_vat', ctx=Store())],
            value=Dict(
                keys=[Constant(value='GR', kind=None)],
                values=[Constant(value='EL', kind=None)],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_eu_country_vat_inverse', ctx=Store())],
            value=DictComp(
                key=Name(id='v', ctx=Load()),
                value=Name(id='k', ctx=Load()),
                generators=[
                    comprehension(
                        target=Tuple(
                            elts=[
                                Name(id='k', ctx=Store()),
                                Name(id='v', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                        iter=Call(
                            func=Attribute(
                                value=Name(id='_eu_country_vat', ctx=Load()),
                                attr='items',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        ifs=[],
                        is_async=0,
                    ),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_ref_vat', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='al', kind=None),
                    Constant(value='ar', kind=None),
                    Constant(value='at', kind=None),
                    Constant(value='au', kind=None),
                    Constant(value='be', kind=None),
                    Constant(value='bg', kind=None),
                    Constant(value='ch', kind=None),
                    Constant(value='cl', kind=None),
                    Constant(value='co', kind=None),
                    Constant(value='cy', kind=None),
                    Constant(value='cz', kind=None),
                    Constant(value='de', kind=None),
                    Constant(value='dk', kind=None),
                    Constant(value='do', kind=None),
                    Constant(value='ec', kind=None),
                    Constant(value='ee', kind=None),
                    Constant(value='el', kind=None),
                    Constant(value='es', kind=None),
                    Constant(value='fi', kind=None),
                    Constant(value='fr', kind=None),
                    Constant(value='gb', kind=None),
                    Constant(value='gr', kind=None),
                    Constant(value='hu', kind=None),
                    Constant(value='hr', kind=None),
                    Constant(value='ie', kind=None),
                    Constant(value='in', kind=None),
                    Constant(value='is', kind=None),
                    Constant(value='it', kind=None),
                    Constant(value='lt', kind=None),
                    Constant(value='lu', kind=None),
                    Constant(value='lv', kind=None),
                    Constant(value='mc', kind=None),
                    Constant(value='mt', kind=None),
                    Constant(value='mx', kind=None),
                    Constant(value='nl', kind=None),
                    Constant(value='no', kind=None),
                    Constant(value='pe', kind=None),
                    Constant(value='pl', kind=None),
                    Constant(value='pt', kind=None),
                    Constant(value='ro', kind=None),
                    Constant(value='rs', kind=None),
                    Constant(value='ru', kind=None),
                    Constant(value='se', kind=None),
                    Constant(value='si', kind=None),
                    Constant(value='sk', kind=None),
                    Constant(value='sm', kind=None),
                    Constant(value='tr', kind=None),
                    Constant(value='xi', kind=None),
                ],
                values=[
                    Constant(value='ALJ91402501L', kind=None),
                    Constant(value='AR200-5536168-2 or 20055361682', kind=None),
                    Constant(value='ATU12345675', kind=None),
                    Constant(value='83 914 571 673', kind=None),
                    Constant(value='BE0477472701', kind=None),
                    Constant(value='BG1234567892', kind=None),
                    Constant(value='CHE-123.456.788 TVA or CHE-123.456.788 MWST or CHE-123.456.788 IVA', kind=None),
                    Constant(value='CL76086428-5', kind=None),
                    Constant(value='CO213123432-1 or CO213.123.432-1', kind=None),
                    Constant(value='CY10259033P', kind=None),
                    Constant(value='CZ12345679', kind=None),
                    Constant(value='DE123456788', kind=None),
                    Constant(value='DK12345674', kind=None),
                    Constant(value='DO1-01-85004-3 or 101850043', kind=None),
                    Constant(value='EC1792060346-001', kind=None),
                    Constant(value='EE123456780', kind=None),
                    Constant(value='EL12345670', kind=None),
                    Constant(value='ESA12345674', kind=None),
                    Constant(value='FI12345671', kind=None),
                    Constant(value='FR23334175221', kind=None),
                    Constant(value='GB123456782 or XI123456782', kind=None),
                    Constant(value='GR12345670', kind=None),
                    Constant(value='HU12345676', kind=None),
                    Constant(value='HR01234567896', kind=None),
                    Constant(value='IE1234567FA', kind=None),
                    Constant(value='12AAAAA1234AAZA', kind=None),
                    Constant(value='IS062199', kind=None),
                    Constant(value='IT12345670017', kind=None),
                    Constant(value='LT123456715', kind=None),
                    Constant(value='LU12345613', kind=None),
                    Constant(value='LV41234567891', kind=None),
                    Constant(value='FR53000004605', kind=None),
                    Constant(value='MT12345634', kind=None),
                    Constant(value='MXGODE561231GR8 or GODE561231GR8', kind=None),
                    Constant(value='NL123456782B90', kind=None),
                    Constant(value='NO123456785', kind=None),
                    Constant(value='10XXXXXXXXY or 20XXXXXXXXY or 15XXXXXXXXY or 16XXXXXXXXY or 17XXXXXXXXY', kind=None),
                    Constant(value='PL1234567883', kind=None),
                    Constant(value='PT123456789', kind=None),
                    Constant(value='RO1234567897', kind=None),
                    Constant(value='RS101134702', kind=None),
                    Constant(value='RU123456789047', kind=None),
                    Constant(value='SE123456789701', kind=None),
                    Constant(value='SI12345679', kind=None),
                    Constant(value='SK2022749619', kind=None),
                    Constant(value='SM24165', kind=None),
                    Constant(value='TR1234567890 (VERGINO) or TR17291716060 (TCKIMLIKNO)', kind=None),
                    Constant(value='XI123456782', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_region_specific_vat_codes', ctx=Store())],
            value=Set(
                elts=[Constant(value='xi', kind=None)],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ResPartner',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='vat', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='VAT/Tax ID', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_split_vat',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='vat_country', ctx=Store()),
                                        Name(id='vat_number', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='vat', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=2, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='vat', ctx=Load()),
                                                slice=Slice(
                                                    lower=Constant(value=2, kind=None),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=' ', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='vat_country', ctx=Load()),
                                    Name(id='vat_number', ctx=Load()),
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
                    name='simple_vat_check',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='country_code', annotation=None, type_comment=None),
                            arg(arg='vat_number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Check the VAT number depending of the country.\n        http://sima-pc.com/nif.php\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Name(id='ustr', ctx=Load()),
                                                    args=[Name(id='country_code', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='encode',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='utf-8', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='isalpha',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='check_func_name', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='check_vat_', kind=None),
                                op=Add(),
                                right=Name(id='country_code', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='check_func', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='check_func_name', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='stdnum', ctx=Load()),
                                                        attr='util',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_cc_module',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='country_code', ctx=Load()),
                                                    Constant(value='vat', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='is_valid', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='check_func', ctx=Load()),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='country_code', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='EU', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='country_code', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_eu_country_vat_inverse', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='country_code', ctx=Load()),
                                            Name(id='country_code', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.country', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='code', kind=None),
                                                                    Constant(value='=ilike', kind=None),
                                                                    Name(id='country_code', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='check_func', ctx=Load()),
                                args=[Name(id='vat_number', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_vies',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='check_vies', ctx=Load()),
                                args=[Name(id='vat', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache',
                                ctx=Load(),
                            ),
                            args=[Constant(value='vat', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='vies_vat_check',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='country_code', annotation=None, type_comment=None),
                            arg(arg='vat_number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='vies_result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_vies',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='country_code', ctx=Load()),
                                                        attr='upper',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Name(id='vat_number', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='vies_result', ctx=Load()),
                                        slice=Constant(value='valid', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='InvalidComponent', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Failed VIES VAT check.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='simple_vat_check',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='country_code', ctx=Load()),
                                                    Name(id='vat_number', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fix_eu_vat_number',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='europe', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.europe', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.country', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='country_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='europe', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='europe', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.country.group', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='Europe', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='europe', ctx=Load()),
                                    Name(id='country', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='country', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='europe', ctx=Load()),
                                                    attr='country_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='vat', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='[^A-Za-z0-9]', kind=None),
                                                    Constant(value='', kind=None),
                                                    Name(id='vat', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='upper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='country_code', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_eu_country_vat', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='country', ctx=Load()),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='country', ctx=Load()),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='upper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='vat', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=2, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='country_code', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='vat', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='country_code', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='vat', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='vat', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='country', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='commercial_partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='country_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_run_vat_test',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='vat',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='country', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Is()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partner_label', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='partner [%s]', kind=None),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='_build_vat_error_message',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='country', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='country', ctx=Load()),
                                                                                attr='code',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='lower',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='vat',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='partner_label', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[Name(id='msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='vat', kind=None),
                                Constant(value='country_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_run_vat_test',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat_number', annotation=None, type_comment=None),
                            arg(arg='default_country', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Checks a VAT number, either syntactically or using VIES, depending\n        on the active company's configuration.\n        A first check is made by using the first two characters of the VAT as\n        the country code. It it fails, a second one is made using default_country instead.\n\n        :param vat_number: a string with the VAT number to check.\n        :param default_country: a res.country object\n\n        :return: The country code (in lower case) of the country the VAT number\n                 was validated for, if it was validated. False if it could not be validated\n                 against the provided or guessed country. None if no country was available\n                 for the check, and no conclusion could be made with certainty.\n        ", kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='company_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='eu_countries', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='base.europe', kind=None)],
                                    keywords=[],
                                ),
                                attr='country_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='vat_check_vies',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Name(id='default_country', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='eu_countries', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='check_func', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='vies_vat_check',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='check_func', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='simple_vat_check',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='check_result', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='vat_country_code', ctx=Store()),
                                        Name(id='vat_number_split', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_split_vat',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vat_number', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vat_has_legit_country_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.country', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='code', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='vat_country_code', ctx=Load()),
                                                            attr='upper',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='vat_has_legit_country_code', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='vat_has_legit_country_code', ctx=Store())],
                                    value=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='vat_country_code', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='_region_specific_vat_codes', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='vat_has_legit_country_code', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='check_result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='check_func', ctx=Load()),
                                        args=[
                                            Name(id='vat_country_code', ctx=Load()),
                                            Name(id='vat_number_split', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='check_result', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Name(id='vat_country_code', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='default_country', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='check_result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='check_func', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='default_country', ctx=Load()),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='vat_number', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='check_result', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='default_country', ctx=Load()),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='check_result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_build_vat_error_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='country_code', annotation=None, type_comment=None),
                            arg(arg='wrong_vat', annotation=None, type_comment=None),
                            arg(arg='record_label', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='company_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='company_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='expected_format', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_ref_vat', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='country_code', ctx=Load()),
                                    Constant(value="'CC##' (CC=Country Code, ##=VAT Number)", kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='company', ctx=Load()),
                                attr='vat_check_vies',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Constant(value='\n', kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='The VAT number [%(wrong_vat)s] for %(record_label)s either failed the VIES VAT validation check or did not respect the expected format %(expected_format)s.', kind=None)],
                                            keywords=[
                                                keyword(
                                                    arg='wrong_vat',
                                                    value=Name(id='wrong_vat', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='record_label',
                                                    value=Name(id='record_label', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='expected_format',
                                                    value=Name(id='expected_format', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='\n', kind=None),
                                op=Add(),
                                right=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='The VAT number [%(wrong_vat)s] for record_label does not seem to be valid. \nNote: the expected format is %(expected_format)s', kind=None)],
                                    keywords=[
                                        keyword(
                                            arg='wrong_vat',
                                            value=Name(id='wrong_vat', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='record_label',
                                            value=Name(id='record_label', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='expected_format',
                                            value=Name(id='expected_format', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='__check_vat_ch_re', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='E([0-9]{9}|-[0-9]{3}\\.[0-9]{3}\\.[0-9]{3})(MWST|TVA|IVA)$', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_ch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Check Switzerland VAT number.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='__check_vat_ch_re',
                                        ctx=Load(),
                                    ),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vat', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='match', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='num', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='s', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='s', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='match', ctx=Load()),
                                                        attr='group',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=1, kind=None)],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='s', ctx=Load()),
                                                            attr='isdigit',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='factor', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='csum', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=BinOp(
                                                    left=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='num', ctx=Load()),
                                                                slice=Name(id='i', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    op=Mult(),
                                                    right=Subscript(
                                                        value=Name(id='factor', ctx=Load()),
                                                        slice=Name(id='i', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[Constant(value=8, kind=None)],
                                                            keywords=[],
                                                        ),
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
                                    targets=[Name(id='check', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Constant(value=11, kind=None),
                                            op=Sub(),
                                            right=BinOp(
                                                left=Name(id='csum', ctx=Load()),
                                                op=Mod(),
                                                right=Constant(value=11, kind=None),
                                            ),
                                        ),
                                        op=Mod(),
                                        right=Constant(value=11, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Compare(
                                        left=Name(id='check', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='num', ctx=Load()),
                                                        slice=Constant(value=8, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_valid_ruc_ec',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ci', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='stdnum', ctx=Load()),
                                        attr='util',
                                        ctx=Load(),
                                    ),
                                    attr='get_cc_module',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ec', kind=None),
                                    Constant(value='ci', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ruc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='stdnum', ctx=Load()),
                                        attr='util',
                                        ctx=Load(),
                                    ),
                                    attr='get_cc_module',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ec', kind=None),
                                    Constant(value='ruc', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='vat', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=10, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ci', ctx=Load()),
                                            attr='is_valid',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vat', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=13, kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='vat', ctx=Load()),
                                                            slice=Constant(value=2, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='6', kind=None)],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='ci', ctx=Load()),
                                                            attr='is_valid',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vat', ctx=Load()),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=10, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ruc', ctx=Load()),
                                                            attr='is_valid',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='vat', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_ec',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='vat', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='clean', ctx=Load()),
                                                args=[
                                                    Name(id='vat', ctx=Load()),
                                                    Constant(value=' -.', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='upper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='is_valid_ruc_ec',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vat', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_ie_check_char',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='vat', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vat', ctx=Load()),
                                    attr='zfill',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=8, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extra', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='vat', ctx=Load()),
                                    slice=Constant(value=7, kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotIn()],
                                comparators=[Constant(value=' W', kind=None)],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='vat', ctx=Load()),
                                                slice=Constant(value=7, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='isalpha',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='extra', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value=9, kind=None),
                                                op=Mult(),
                                                right=BinOp(
                                                    left=Call(
                                                        func=Name(id='ord', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vat', ctx=Load()),
                                                                slice=Constant(value=7, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    op=Sub(),
                                                    right=Constant(value=64, kind=None),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='checksum', ctx=Store())],
                            value=BinOp(
                                left=Name(id='extra', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='sum', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=BinOp(
                                                left=BinOp(
                                                    left=Constant(value=8, kind=None),
                                                    op=Sub(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                op=Mult(),
                                                right=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='x', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Tuple(
                                                        elts=[
                                                            Name(id='i', ctx=Store()),
                                                            Name(id='x', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                    iter=Call(
                                                        func=Name(id='enumerate', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vat', ctx=Load()),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=7, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Constant(value='WABCDEFGHIJKLMNOPQRSTUV', kind=None),
                                slice=BinOp(
                                    left=Name(id='checksum', ctx=Load()),
                                    op=Mod(),
                                    right=Constant(value=23, kind=None),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_ie',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Temporary Ireland VAT validation to support the new format\n        introduced in January 2013 in Ireland, until upstream is fixed.\n        TODO: remove when fixed upstream', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=8, kind=None),
                                                    Constant(value=9, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='vat', ctx=Load()),
                                                    slice=Slice(
                                                        lower=Constant(value=2, kind=None),
                                                        upper=Constant(value=7, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                attr='isdigit',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='vat', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=8, kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='vat', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=' ', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='vat', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=7, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='isdigit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Compare(
                                        left=Subscript(
                                            value=Name(id='vat', ctx=Load()),
                                            slice=Constant(value=7, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_ie_check_char',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Subscript(
                                                            value=Name(id='vat', ctx=Load()),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=Constant(value=7, kind=None),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Name(id='vat', ctx=Load()),
                                                            slice=Constant(value=8, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='vat', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='string', ctx=Load()),
                                                    attr='ascii_uppercase',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='+*', kind=None),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Compare(
                                                left=Subscript(
                                                    value=Name(id='vat', ctx=Load()),
                                                    slice=Constant(value=7, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_ie_check_char',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Subscript(
                                                                        value=Name(id='vat', ctx=Load()),
                                                                        slice=Slice(
                                                                            lower=Constant(value=2, kind=None),
                                                                            upper=Constant(value=7, kind=None),
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Subscript(
                                                                        value=Name(id='vat', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Name(id='vat', ctx=Load()),
                                                                    slice=Constant(value=8, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='__check_vat_mx_re', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value=b'(?P<primeras>[A-Za-z\\xd1\\xf1&]{3,4})[ \\-_]?(?P<ano>[0-9]{2})(?P<mes>[01][0-9])(?P<dia>[0-3][0-9])[ \\-_]?(?P<code>[A-Za-z0-9&\\xd1\\xf1]{3})$', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_mx',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Mexican VAT verification\n\n        Verificar RFC México\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='vat', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='ustr', ctx=Load()),
                                        args=[Name(id='vat', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='iso8859-1', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='m', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='__check_vat_mx_re',
                                        ctx=Load(),
                                    ),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vat', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='m', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='ano', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ano', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='ano', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=30, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='ano', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value=1900, kind=None),
                                                op=Add(),
                                                right=Name(id='ano', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='ano', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value=2000, kind=None),
                                                op=Add(),
                                                right=Name(id='ano', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ano', ctx=Load()),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='m', ctx=Load()),
                                                            attr='group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='mes', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='m', ctx=Load()),
                                                            attr='group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='dia', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='__check_vat_nl_re', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='(?:NL)?[0-9A-Z+*]{10}[0-9]{2}', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_nl',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Temporary Netherlands VAT validation to support the new format introduced in January 2020,\n        until upstream is fixed.\n\n        Algorithm detail: http://kleineondernemer.nl/index.php/nieuw-btw-identificatienummer-vanaf-1-januari-2020-voor-eenmanszaken\n\n        TODO: remove when fixed upstream\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                ImportFrom(
                                    module='stdnum.util',
                                    names=[alias(name='clean', asname=None)],
                                    level=0,
                                ),
                                ImportFrom(
                                    module='stdnum.nl.bsn',
                                    names=[alias(name='checksum', asname=None)],
                                    level=0,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ImportError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='vat', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='clean', ctx=Load()),
                                                args=[
                                                    Name(id='vat', ctx=Load()),
                                                    Constant(value=' -.', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='upper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='vat', ctx=Load()),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='NL', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='vat', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='vat', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=2, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='vat', ctx=Load())],
                                        keywords=[],
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value=12, kind=None)],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='match', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='__check_vat_nl_re',
                                        ctx=Load(),
                                    ),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vat', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='match', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='char_to_int', ctx=Store())],
                            value=DictComp(
                                key=Name(id='k', ctx=Load()),
                                value=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=Call(
                                                func=Name(id='ord', ctx=Load()),
                                                args=[Name(id='k', ctx=Load())],
                                                keywords=[],
                                            ),
                                            op=Sub(),
                                            right=Constant(value=55, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='k', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='string', ctx=Load()),
                                            attr='ascii_uppercase',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='char_to_int', ctx=Load()),
                                    slice=Constant(value='+', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='36', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='char_to_int', ctx=Load()),
                                    slice=Constant(value='*', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='37', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='check_val_natural', ctx=Store())],
                            value=Constant(value='2321', kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='x', ctx=Store()),
                            iter=Name(id='vat', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='check_val_natural', ctx=Store()),
                                    op=Add(),
                                    value=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='isdigit',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        body=Name(id='x', ctx=Load()),
                                        orelse=Subscript(
                                            value=Name(id='char_to_int', ctx=Load()),
                                            slice=Name(id='x', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=BinOp(
                                    left=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='check_val_natural', ctx=Load())],
                                        keywords=[],
                                    ),
                                    op=Mod(),
                                    right=Constant(value=97, kind=None),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='vat', ctx=Store())],
                            value=Subscript(
                                value=Name(id='vat', ctx=Load()),
                                slice=Slice(
                                    lower=None,
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=3, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vat', ctx=Load()),
                                            attr='isdigit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='checksum', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_no',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Check Norway VAT number.See http://www.brreg.no/english/coordination/number.html\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=12, kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='vat', ctx=Load()),
                                                    attr='upper',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='MVA', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='vat', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='vat', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=3, kind=None),
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
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='vat', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value=9, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='vat', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='sum', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value=3, kind=None),
                                                            op=Mult(),
                                                            right=Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='vat', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=BinOp(
                                                            left=Constant(value=2, kind=None),
                                                            op=Mult(),
                                                            right=Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='vat', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=BinOp(
                                                        left=Constant(value=7, kind=None),
                                                        op=Mult(),
                                                        right=Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='vat', ctx=Load()),
                                                                    slice=Constant(value=2, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Constant(value=6, kind=None),
                                                    op=Mult(),
                                                    right=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vat', ctx=Load()),
                                                                slice=Constant(value=3, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ),
                                            op=Add(),
                                            right=BinOp(
                                                left=Constant(value=5, kind=None),
                                                op=Mult(),
                                                right=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='vat', ctx=Load()),
                                                            slice=Constant(value=4, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                        op=Add(),
                                        right=BinOp(
                                            left=Constant(value=4, kind=None),
                                            op=Mult(),
                                            right=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Constant(value=5, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                    op=Add(),
                                    right=BinOp(
                                        left=Constant(value=3, kind=None),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='vat', ctx=Load()),
                                                    slice=Constant(value=6, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Constant(value=2, kind=None),
                                    op=Mult(),
                                    right=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='vat', ctx=Load()),
                                                slice=Constant(value=7, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='check', ctx=Store())],
                            value=BinOp(
                                left=Constant(value=11, kind=None),
                                op=Sub(),
                                right=BinOp(
                                    left=Name(id='sum', ctx=Load()),
                                    op=Mod(),
                                    right=Constant(value=11, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='check', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=11, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='check', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='check', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=10, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Compare(
                                left=Name(id='check', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='vat', ctx=Load()),
                                                slice=Constant(value=8, kind=None),
                                                ctx=Load(),
                                            ),
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
                    name='check_vat_pe',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=11, kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='vat', ctx=Load()),
                                                attr='isdigit',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='dig_check', ctx=Store())],
                            value=BinOp(
                                left=Constant(value=11, kind=None),
                                op=Sub(),
                                right=BinOp(
                                    left=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=BinOp(
                                                    left=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Constant(value='5432765432', kind=None),
                                                                slice=Name(id='f', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    op=Mult(),
                                                    right=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vat', ctx=Load()),
                                                                slice=Name(id='f', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='f', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[
                                                                Constant(value=0, kind=None),
                                                                Constant(value=10, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    op=Mod(),
                                    right=Constant(value=11, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='dig_check', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=10, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dig_check', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='dig_check', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=11, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='dig_check', ctx=Store())],
                                            value=Constant(value=1, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Compare(
                                left=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='vat', ctx=Load()),
                                            slice=Constant(value=10, kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Name(id='dig_check', ctx=Load())],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_ru',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Check Russia VAT number.\n        Method copied from vatnumber 1.2 lib https://code.google.com/archive/p/vatnumber/\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=10, kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=12, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='vat', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='vat', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=10, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='check_sum', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=Constant(value=2, kind=None),
                                                                        op=Mult(),
                                                                        right=Call(
                                                                            func=Name(id='int', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='vat', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    op=Add(),
                                                                    right=BinOp(
                                                                        left=Constant(value=4, kind=None),
                                                                        op=Mult(),
                                                                        right=Call(
                                                                            func=Name(id='int', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='vat', ctx=Load()),
                                                                                    slice=Constant(value=1, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=BinOp(
                                                                    left=Constant(value=10, kind=None),
                                                                    op=Mult(),
                                                                    right=Call(
                                                                        func=Name(id='int', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='vat', ctx=Load()),
                                                                                slice=Constant(value=2, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=BinOp(
                                                                left=Constant(value=3, kind=None),
                                                                op=Mult(),
                                                                right=Call(
                                                                    func=Name(id='int', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='vat', ctx=Load()),
                                                                            slice=Constant(value=3, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=BinOp(
                                                            left=Constant(value=5, kind=None),
                                                            op=Mult(),
                                                            right=Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='vat', ctx=Load()),
                                                                        slice=Constant(value=4, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=BinOp(
                                                        left=Constant(value=9, kind=None),
                                                        op=Mult(),
                                                        right=Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='vat', ctx=Load()),
                                                                    slice=Constant(value=5, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Constant(value=4, kind=None),
                                                    op=Mult(),
                                                    right=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vat', ctx=Load()),
                                                                slice=Constant(value=6, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ),
                                            op=Add(),
                                            right=BinOp(
                                                left=Constant(value=6, kind=None),
                                                op=Mult(),
                                                right=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='vat', ctx=Load()),
                                                            slice=Constant(value=7, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                        op=Add(),
                                        right=BinOp(
                                            left=Constant(value=8, kind=None),
                                            op=Mult(),
                                            right=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Constant(value=8, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='check', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='check_sum', ctx=Load()),
                                        op=Mod(),
                                        right=Constant(value=11, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='check', ctx=Load()),
                                            op=Mod(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Constant(value=9, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='check_sum1', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=BinOp(
                                                                            left=Constant(value=7, kind=None),
                                                                            op=Mult(),
                                                                            right=Call(
                                                                                func=Name(id='int', ctx=Load()),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='vat', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        op=Add(),
                                                                        right=BinOp(
                                                                            left=Constant(value=2, kind=None),
                                                                            op=Mult(),
                                                                            right=Call(
                                                                                func=Name(id='int', ctx=Load()),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='vat', ctx=Load()),
                                                                                        slice=Constant(value=1, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ),
                                                                    op=Add(),
                                                                    right=BinOp(
                                                                        left=Constant(value=4, kind=None),
                                                                        op=Mult(),
                                                                        right=Call(
                                                                            func=Name(id='int', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='vat', ctx=Load()),
                                                                                    slice=Constant(value=2, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=BinOp(
                                                                    left=Constant(value=10, kind=None),
                                                                    op=Mult(),
                                                                    right=Call(
                                                                        func=Name(id='int', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='vat', ctx=Load()),
                                                                                slice=Constant(value=3, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=BinOp(
                                                                left=Constant(value=3, kind=None),
                                                                op=Mult(),
                                                                right=Call(
                                                                    func=Name(id='int', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='vat', ctx=Load()),
                                                                            slice=Constant(value=4, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=BinOp(
                                                            left=Constant(value=5, kind=None),
                                                            op=Mult(),
                                                            right=Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='vat', ctx=Load()),
                                                                        slice=Constant(value=5, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=BinOp(
                                                        left=Constant(value=9, kind=None),
                                                        op=Mult(),
                                                        right=Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='vat', ctx=Load()),
                                                                    slice=Constant(value=6, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Constant(value=4, kind=None),
                                                    op=Mult(),
                                                    right=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vat', ctx=Load()),
                                                                slice=Constant(value=7, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ),
                                            op=Add(),
                                            right=BinOp(
                                                left=Constant(value=6, kind=None),
                                                op=Mult(),
                                                right=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='vat', ctx=Load()),
                                                            slice=Constant(value=8, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                        op=Add(),
                                        right=BinOp(
                                            left=Constant(value=8, kind=None),
                                            op=Mult(),
                                            right=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Constant(value=9, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='check', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='check_sum1', ctx=Load()),
                                        op=Mod(),
                                        right=Constant(value=11, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='check', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Constant(value=10, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='check_sum2', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=BinOp(
                                                                            left=BinOp(
                                                                                left=Constant(value=3, kind=None),
                                                                                op=Mult(),
                                                                                right=Call(
                                                                                    func=Name(id='int', ctx=Load()),
                                                                                    args=[
                                                                                        Subscript(
                                                                                            value=Name(id='vat', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                            op=Add(),
                                                                            right=BinOp(
                                                                                left=Constant(value=7, kind=None),
                                                                                op=Mult(),
                                                                                right=Call(
                                                                                    func=Name(id='int', ctx=Load()),
                                                                                    args=[
                                                                                        Subscript(
                                                                                            value=Name(id='vat', ctx=Load()),
                                                                                            slice=Constant(value=1, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                        ),
                                                                        op=Add(),
                                                                        right=BinOp(
                                                                            left=Constant(value=2, kind=None),
                                                                            op=Mult(),
                                                                            right=Call(
                                                                                func=Name(id='int', ctx=Load()),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='vat', ctx=Load()),
                                                                                        slice=Constant(value=2, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ),
                                                                    op=Add(),
                                                                    right=BinOp(
                                                                        left=Constant(value=4, kind=None),
                                                                        op=Mult(),
                                                                        right=Call(
                                                                            func=Name(id='int', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='vat', ctx=Load()),
                                                                                    slice=Constant(value=3, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=BinOp(
                                                                    left=Constant(value=10, kind=None),
                                                                    op=Mult(),
                                                                    right=Call(
                                                                        func=Name(id='int', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='vat', ctx=Load()),
                                                                                slice=Constant(value=4, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=BinOp(
                                                                left=Constant(value=3, kind=None),
                                                                op=Mult(),
                                                                right=Call(
                                                                    func=Name(id='int', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='vat', ctx=Load()),
                                                                            slice=Constant(value=5, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=BinOp(
                                                            left=Constant(value=5, kind=None),
                                                            op=Mult(),
                                                            right=Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='vat', ctx=Load()),
                                                                        slice=Constant(value=6, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=BinOp(
                                                        left=Constant(value=9, kind=None),
                                                        op=Mult(),
                                                        right=Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='vat', ctx=Load()),
                                                                    slice=Constant(value=7, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Constant(value=4, kind=None),
                                                    op=Mult(),
                                                    right=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vat', ctx=Load()),
                                                                slice=Constant(value=8, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ),
                                            op=Add(),
                                            right=BinOp(
                                                left=Constant(value=6, kind=None),
                                                op=Mult(),
                                                right=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='vat', ctx=Load()),
                                                            slice=Constant(value=9, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                        op=Add(),
                                        right=BinOp(
                                            left=Constant(value=8, kind=None),
                                            op=Mult(),
                                            right=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Constant(value=10, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='check', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='check_sum2', ctx=Load()),
                                        op=Mod(),
                                        right=Constant(value=11, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='check', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Constant(value=11, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_tr',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=Constant(value=10, kind=None),
                                    ops=[
                                        LtE(),
                                        LtE(),
                                    ],
                                    comparators=[
                                        Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Constant(value=11, kind=None),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='vat', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='vat', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=10, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sum', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='check', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='f', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Constant(value=9, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='c1', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vat', ctx=Load()),
                                                                slice=Name(id='f', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    op=Add(),
                                                    right=BinOp(
                                                        left=Constant(value=9, kind=None),
                                                        op=Sub(),
                                                        right=Name(id='f', ctx=Load()),
                                                    ),
                                                ),
                                                op=Mod(),
                                                right=Constant(value=10, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='c2', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Name(id='c1', ctx=Load()),
                                                    op=Mult(),
                                                    right=BinOp(
                                                        left=Constant(value=2, kind=None),
                                                        op=Pow(),
                                                        right=BinOp(
                                                            left=Constant(value=9, kind=None),
                                                            op=Sub(),
                                                            right=Name(id='f', ctx=Load()),
                                                        ),
                                                    ),
                                                ),
                                                op=Mod(),
                                                right=Constant(value=9, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='c1', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='c2', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='c2', ctx=Store())],
                                                    value=Constant(value=9, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='sum', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='c2', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='sum', ctx=Load()),
                                            op=Mod(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='check', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='check', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value=10, kind=None),
                                                op=Sub(),
                                                right=BinOp(
                                                    left=Name(id='sum', ctx=Load()),
                                                    op=Mod(),
                                                    right=Constant(value=10, kind=None),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Return(
                                    value=Compare(
                                        left=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='vat', ctx=Load()),
                                                    slice=Constant(value=9, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='check', ctx=Load())],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='vat', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=11, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='c1a', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='c1b', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='c2', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='f', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='c1a', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Name(id='f', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='f', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=1, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='c1b', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Name(id='f', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='c1', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Constant(value=7, kind=None),
                                                op=Mult(),
                                                right=Name(id='c1a', ctx=Load()),
                                            ),
                                            op=Sub(),
                                            right=Name(id='c1b', ctx=Load()),
                                        ),
                                        op=Mod(),
                                        right=Constant(value=10, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='f', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='c2', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vat', ctx=Load()),
                                                        slice=Name(id='f', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='c2', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='c2', ctx=Load()),
                                        op=Mod(),
                                        right=Constant(value=10, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='vat', ctx=Load()),
                                                            slice=Constant(value=9, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='c1', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='vat', ctx=Load()),
                                                            slice=Constant(value=10, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='c2', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_ua',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='commercial_partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='MX', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='vat', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=10, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='res', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=True, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='res', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=False, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='commercial_partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='is_company',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='vat', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=12, kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=True, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=False, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='vat', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=10, kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='vat', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=9, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=True, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=False, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='all', ctx=Load()),
                                args=[Name(id='res', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_xi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Temporary Nothern Ireland VAT validation following Brexit\n        As of January 1st 2021, companies in Northern Ireland have a\n        new VAT number starting with XI\n        TODO: remove when stdnum is updated to 1.16 in supported distro', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='check_func', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='stdnum', ctx=Load()),
                                                attr='util',
                                                ctx=Load(),
                                            ),
                                            attr='get_cc_module',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='gb', kind=None),
                                            Constant(value='vat', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='is_valid', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='check_func', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=9, kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='check_func', ctx=Load()),
                                args=[Name(id='vat', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_in',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='vat', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='vat', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=15, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='all_gstin_re', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='[0-9]{2}[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[Zz1-9A-Ja-j]{1}[0-9a-zA-Z]{1}', kind=None),
                                            Constant(value='[0-9]{4}[A-Z]{3}[0-9]{5}[UO]{1}[N][A-Z0-9]{1}', kind=None),
                                            Constant(value='[0-9]{4}[a-zA-Z]{3}[0-9]{5}[N][R][0-9a-zA-Z]{1}', kind=None),
                                            Constant(value='[0-9]{2}[a-zA-Z]{4}[a-zA-Z0-9]{1}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[DK]{1}[0-9a-zA-Z]{1}', kind=None),
                                            Constant(value='[0-9]{2}[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[C]{1}[0-9a-zA-Z]{1}', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='re', ctx=Load()),
                                                                attr='compile',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='rx', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='match',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='vat', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='rx', ctx=Store()),
                                                        iter=Name(id='all_gstin_re', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_vat_au',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        The Australian equivalent of a VAT number is an ABN number.\n        TFN (Australia Tax file numbers) are private and not to be\n        entered into systems or publicly displayed, so ABN numbers\n        are the public facing number that legally must be displayed\n        on all invoices\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='check_func', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='stdnum', ctx=Load()),
                                                attr='util',
                                                ctx=Load(),
                                            ),
                                            attr='get_cc_module',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='au', kind=None),
                                            Constant(value='abn', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='is_valid', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='check_func', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='vat', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vat', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=' ', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='vat', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=11, kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vat', ctx=Load()),
                                                    attr='isdigit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='check_func', ctx=Load()),
                                args=[Name(id='vat', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='format_vat_ch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='stdnum_vat_format', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='stdnum', ctx=Load()),
                                                attr='util',
                                                ctx=Load(),
                                            ),
                                            attr='get_cc_module',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='ch', kind=None),
                                            Constant(value='vat', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='format', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id='stdnum_vat_format', ctx=Load()),
                                body=Subscript(
                                    value=Call(
                                        func=Name(id='stdnum_vat_format', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='CH', kind=None),
                                                op=Add(),
                                                right=Name(id='vat', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    slice=Slice(
                                        lower=Constant(value=2, kind=None),
                                        upper=None,
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                orelse=Name(id='vat', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_fix_vat_number',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vat', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=IfExp(
                                test=Name(id='country_id', ctx=Load()),
                                body=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.country', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='country_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='vat_country', ctx=Store()),
                                        Name(id='vat_number', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_split_vat',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vat', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='code', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='code', ctx=Load()),
                                                attr='lower',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='vat_country', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='vat', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='stdnum_vat_fix_func', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='stdnum', ctx=Load()),
                                                attr='util',
                                                ctx=Load(),
                                            ),
                                            attr='get_cc_module',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='vat_country', ctx=Load()),
                                            Constant(value='vat', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='compact', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='format_func_name', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='format_vat_', kind=None),
                                op=Add(),
                                right=Name(id='vat_country', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='format_func', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='format_func_name', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='stdnum_vat_fix_func', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='format_func', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='vat_number', ctx=Store())],
                                    value=Call(
                                        func=Name(id='format_func', ctx=Load()),
                                        args=[Name(id='vat_number', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='vat_country', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Name(id='vat_number', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='vat', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='country_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='country_id', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='vat', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_fix_vat_number',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='vat', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='country_id', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResPartner', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='vat', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='country_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='country_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='country_id', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='vat', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_fix_vat_number',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='vat', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='country_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResPartner', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)

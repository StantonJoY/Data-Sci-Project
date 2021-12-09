Module(
    body=[
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[
                alias(name='sql', asname=None),
                alias(name='DatabaseError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='DEFAULT_SERVER_DATETIME_FORMAT', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.res_partner',
            names=[
                alias(name='WARNING_MESSAGE', asname=None),
                alias(name='WARNING_HELP', asname=None),
            ],
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
        ClassDef(
            name='AccountFiscalPosition',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account.fiscal.position', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Fiscal Position', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
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
                                value=Constant(value='Fiscal Position', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='By unchecking the active field, you may hide a fiscal position without deleting it.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='res.company', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='account_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.fiscal.position.account', kind=None),
                            Constant(value='position_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Account Mapping', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tax_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.fiscal.position.tax', kind=None),
                            Constant(value='position_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Tax Mapping', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='note', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Notes', kind=None)],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Legal mentions that have to be printed on the invoices.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='auto_apply', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Detect Automatically', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Apply automatically this fiscal position.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='vat_required', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='VAT required', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Apply only if partner has a VAT number.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_country_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company Country', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.account_fiscal_country_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='country_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.country', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Country', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Apply only if delivery country matches.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='country_group_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.country.group', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Country Group', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Apply only if delivery country matches the group.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.country.state', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Federal States', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='zip_from', ctx=Store())],
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
                                value=Constant(value='Zip Range From', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='zip_to', ctx=Store())],
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
                                value=Constant(value='Zip Range To', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='states_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_states_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='foreign_vat', ctx=Store())],
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
                                value=Constant(value='Foreign Tax ID', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The tax ID of your company in the region mapped by this fiscal position.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='foreign_vat_header_mode', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='templates_found', kind=None),
                                                Constant(value='Templates Found', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='no_template', kind=None),
                                                Constant(value='No Template', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_foreign_vat_header_mode', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field used to display a banner on top of foreign vat fiscal positions, in order to ease the instantiation of foreign taxes when possible.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_states_count',
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
                            target=Name(id='position', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='position', ctx=Load()),
                                            attr='states_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='position', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='state_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_foreign_vat_header_mode',
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
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='foreign_vat',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='foreign_vat_header_mode',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.tax', kind=None),
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
                                                            Constant(value='country_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='country_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
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
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='foreign_vat_header_mode',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.tax.template', kind=None),
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
                                                                    Constant(value='chart_template_id.country_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='country_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
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
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='foreign_vat_header_mode',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='templates_found', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='foreign_vat_header_mode',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='no_template', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
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
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='foreign_vat', kind=None),
                                Constant(value='country_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_zip',
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
                            target=Name(id='position', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='position', ctx=Load()),
                                                attr='zip_from',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='position', ctx=Load()),
                                                attr='zip_to',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='position', ctx=Load()),
                                                    attr='zip_from',
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='position', ctx=Load()),
                                                        attr='zip_to',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Invalid "Zip Range", please configure it properly.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
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
                                Constant(value='zip_from', kind=None),
                                Constant(value='zip_to', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_validate_foreign_vat_country',
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
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='foreign_vat',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='account_fiscal_country_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='foreign_vat',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='vat',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValidationError', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='You cannot create a fiscal position within your fiscal country with the same VAT number as the main one set on your company.', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='state_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        attr='company_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='account_fiscal_country_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='state_ids',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Name(id='ValidationError', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='You cannot create a fiscal position with a foreign VAT within your fiscal country without assigning it a state.', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    cause=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Name(id='ValidationError', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='You cannot create a fiscal position with a foreign VAT within your fiscal country.', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    cause=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='similar_fpos_domain', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='foreign_vat', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='country_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='country_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='state_ids',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='similar_fpos_domain', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state_ids', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='state_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='similar_fpos_count', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.fiscal.position', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search_count',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='similar_fpos_domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='similar_fpos_count', ctx=Load()),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='A fiscal position with a foreign VAT already exists in this region.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
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
                                Constant(value='country_id', kind=None),
                                Constant(value='state_ids', kind=None),
                                Constant(value='foreign_vat', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='map_tax',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='taxes', annotation=None, type_comment=None),
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
                                operand=Name(id='self', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='taxes', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.tax', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='tax', ctx=Store()),
                            iter=Name(id='taxes', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='taxes_correspondance', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tax_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='t', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='tax_src_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='tax', ctx=Load()),
                                                            attr='_origin',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='result', ctx=Store()),
                                    op=BitOr(),
                                    value=IfExp(
                                        test=Name(id='taxes_correspondance', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='taxes_correspondance', ctx=Load()),
                                            attr='tax_dest_id',
                                            ctx=Load(),
                                        ),
                                        orelse=Name(id='tax', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='map_account',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='account', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='pos', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='account_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='pos', ctx=Load()),
                                            attr='account_src_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='account', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Name(id='pos', ctx=Load()),
                                                attr='account_dest_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='account', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='map_accounts',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='accounts', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Receive a dictionary having accounts in values and try to replace those accounts accordingly to the fiscal position.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ref_dict', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='account_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='ref_dict', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='account_src_id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='account_dest_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='acc', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='accounts', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='acc', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='ref_dict', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='accounts', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='ref_dict', ctx=Load()),
                                                slice=Name(id='acc', ctx=Load()),
                                                ctx=Load(),
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
                            value=Name(id='accounts', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_country_id',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='country_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='zip_from',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='zip_to',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='country_group_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='state_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[Constant(value=5, kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='states_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='state_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='country_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_country_group_id',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='country_group_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='zip_from',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='zip_to',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='country_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='state_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[Constant(value=5, kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='country_group_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_convert_zip_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='zip_from', annotation=None, type_comment=None),
                            arg(arg='zip_to', annotation=None, type_comment=None),
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
                        Assign(
                            targets=[Name(id='max_length', ctx=Store())],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='zip_from', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='zip_to', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='zip_from', ctx=Load()),
                                    attr='isdigit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='zip_from', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='zip_from', ctx=Load()),
                                            attr='rjust',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='max_length', ctx=Load()),
                                            Constant(value='0', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='zip_to', ctx=Load()),
                                    attr='isdigit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='zip_to', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='zip_to', ctx=Load()),
                                            attr='rjust',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='max_length', ctx=Load()),
                                            Constant(value='0', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='zip_from', ctx=Load()),
                                    Name(id='zip_to', ctx=Load()),
                                ],
                                ctx=Load(),
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
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='zip_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='zip_from', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='zip_to', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='zip_to', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='zip_from', ctx=Load()),
                                    Name(id='zip_to', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='zip_from', kind=None),
                                                    ctx=Store(),
                                                ),
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='zip_to', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_convert_zip_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='zip_from', ctx=Load()),
                                            Name(id='zip_to', ctx=Load()),
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
                                            Name(id='AccountFiscalPosition', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='zip_from', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='zip_from', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='zip_to', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='zip_to', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='zip_from', ctx=Load()),
                                    Name(id='zip_to', ctx=Load()),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='rec', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Constant(value='zip_from', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Constant(value='zip_to', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_convert_zip_values',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='zip_from', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='rec', ctx=Load()),
                                                                attr='zip_from',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='zip_to', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='rec', ctx=Load()),
                                                                attr='zip_to',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                                            Name(id='AccountFiscalPosition', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_fpos_by_region',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                            arg(arg='state_id', annotation=None, type_comment=None),
                            arg(arg='zipcode', annotation=None, type_comment=None),
                            arg(arg='vat_required', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='country_id', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='base_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='auto_apply', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='vat_required', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='vat_required', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value='in', kind=None),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='null_state_dom', ctx=Store()),
                                Name(id='state_domain', ctx=Store()),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='state_ids', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='null_zip_dom', ctx=Store()),
                                Name(id='zip_domain', ctx=Store()),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='zip_from', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='zip_to', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='null_country_dom', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='country_group_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='zipcode', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='zip_domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='zip_from', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='zipcode', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='zip_to', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Name(id='zipcode', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='state_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='state_domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='state_ids', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='state_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain_country', ctx=Store())],
                            value=BinOp(
                                left=Name(id='base_domain', ctx=Load()),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='country_id', kind=None),
                                                Constant(value='=', kind=None),
                                                Name(id='country_id', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain_group', ctx=Store())],
                            value=BinOp(
                                left=Name(id='base_domain', ctx=Load()),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='country_group_id.country_ids', kind=None),
                                                Constant(value='=', kind=None),
                                                Name(id='country_id', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fpos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='domain_country', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='state_domain', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='zip_domain', ctx=Load()),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='fpos', ctx=Load()),
                                    ),
                                    Name(id='state_id', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fpos', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='domain_country', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='null_state_dom', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='zip_domain', ctx=Load()),
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
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='fpos', ctx=Load()),
                                    ),
                                    Name(id='zipcode', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fpos', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='domain_country', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='state_domain', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='null_zip_dom', ctx=Load()),
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
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='fpos', ctx=Load()),
                                    ),
                                    Name(id='state_id', ctx=Load()),
                                    Name(id='zipcode', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fpos', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='domain_country', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='null_state_dom', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='null_zip_dom', ctx=Load()),
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='fpos', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fpos', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='domain_group', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='null_state_dom', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='null_zip_dom', ctx=Load()),
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='fpos', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fpos', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='base_domain', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='null_country_dom', ctx=Load()),
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
                        Return(
                            value=Name(id='fpos', ctx=Load()),
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
                    name='get_fiscal_position',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                            arg(arg='delivery_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :return: fiscal position found (recordset)\n        :rtype: :class:`account.fiscal.position`\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='partner_id', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='PartnerObj', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='PartnerObj', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='partner_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='delivery_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='delivery', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='PartnerObj', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='delivery_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='delivery', ctx=Store())],
                                    value=Name(id='partner', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='delivery', ctx=Load()),
                                        attr='property_account_position_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='property_account_position_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='delivery', ctx=Load()),
                                                attr='property_account_position_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='property_account_position_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='vat_required', ctx=Store())],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='vat',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fp', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_fpos_by_region',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='delivery', ctx=Load()),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='delivery', ctx=Load()),
                                            attr='state_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='delivery', ctx=Load()),
                                        attr='zip',
                                        ctx=Load(),
                                    ),
                                    Name(id='vat_required', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='fp', ctx=Load()),
                                    ),
                                    Name(id='vat_required', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fp', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_fpos_by_region',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='delivery', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='delivery', ctx=Load()),
                                                    attr='state_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='delivery', ctx=Load()),
                                                attr='zip',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='fp', ctx=Load()),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.fiscal.position', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                    name='action_create_foreign_taxes',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_try_instantiating_foreign_taxes',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='country_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AccountFiscalPositionTax',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account.fiscal.position.tax', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Tax Mapping of Fiscal Position', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='position_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_check_company_auto', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='position_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.fiscal.position', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Fiscal Position', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='position_id.company_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tax_src_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.tax', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Tax on Product', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tax_dest_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.tax', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Tax to Apply', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='tax_src_dest_uniq', kind=None),
                                    Constant(value='unique (position_id,tax_src_id,tax_dest_id)', kind=None),
                                    Constant(value='A tax fiscal position could be defined only one time on same taxes.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AccountFiscalPositionAccount',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account.fiscal.position.account', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Accounts Mapping of Fiscal Position', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='position_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_check_company_auto', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='position_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.fiscal.position', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Fiscal Position', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='position_id.company_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='account_src_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Account on Product', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('deprecated', '=', False), ('company_id', '=', company_id)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='account_dest_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Account to Use Instead', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('deprecated', '=', False), ('company_id', '=', company_id)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='account_src_dest_uniq', kind=None),
                                    Constant(value='unique (position_id,account_src_id,account_dest_id)', kind=None),
                                    Constant(value='An account fiscal position could be defined only one time on same accounts.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.partner', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_credit_debit_get',
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
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='tables', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='state',
                                                value=Constant(value='posted', kind=None),
                                            ),
                                            keyword(
                                                arg='company_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='_query_get',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='where_params', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Call(
                                            func=Name(id='tuple', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Name(id='where_params', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='where_clause', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='where_clause', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='AND ', kind=None),
                                        op=Add(),
                                        right=Name(id='where_clause', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=Constant(value='SELECT account_move_line.partner_id, act.type, SUM(account_move_line.amount_residual)\n                      FROM ', kind=None),
                                                    op=Add(),
                                                    right=Name(id='tables', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Constant(value="\n                      LEFT JOIN account_account a ON (account_move_line.account_id=a.id)\n                      LEFT JOIN account_account_type act ON (a.user_type_id=act.id)\n                      WHERE act.type IN ('receivable','payable')\n                      AND account_move_line.partner_id IN %s\n                      AND account_move_line.reconciled IS NOT TRUE\n                      ", kind=None),
                                            ),
                                            op=Add(),
                                            right=Name(id='where_clause', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Constant(value='\n                      GROUP BY account_move_line.partner_id, act.type\n                      ', kind=None),
                                    ),
                                    Name(id='where_params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='treated', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='pid', ctx=Store()),
                                    Name(id='type', ctx=Store()),
                                    Name(id='val', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='receivable', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='credit',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='val', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='partner', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='treated', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='debit',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='treated', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Name(id='partner', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='payable', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='debit',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=UnaryOp(
                                                        op=USub(),
                                                        operand=Name(id='val', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='partner', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='treated', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='credit',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=False, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='treated', ctx=Store()),
                                                            op=BitOr(),
                                                            value=Name(id='partner', ctx=Load()),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remaining', ctx=Store())],
                            value=BinOp(
                                left=Name(id='self', ctx=Load()),
                                op=Sub(),
                                right=Name(id='treated', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='remaining', ctx=Load()),
                                    attr='debit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='remaining', ctx=Load()),
                                    attr='credit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends_context',
                                ctx=Load(),
                            ),
                            args=[Constant(value='company', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_asset_difference_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='account_type', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='operand', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='operator', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='<', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='>', kind=None),
                                            Constant(value='>=', kind=None),
                                            Constant(value='<=', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='type', ctx=Load()),
                                    args=[Name(id='operand', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[NotIn()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Name(id='float', ctx=Load()),
                                            Name(id='int', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='sign', ctx=Store())],
                            value=Constant(value=1, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='account_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='payable', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sign', ctx=Store())],
                                    value=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Constant(value="\n            SELECT partner.id\n            FROM res_partner partner\n            LEFT JOIN account_move_line aml ON aml.partner_id = partner.id\n            JOIN account_move move ON move.id = aml.move_id\n            RIGHT JOIN account_account acc ON aml.account_id = acc.id\n            WHERE acc.internal_type = %s\n              AND NOT acc.deprecated AND acc.company_id = %s\n              AND move.state = 'posted'\n            GROUP BY partner.id\n            HAVING %s * COALESCE(SUM(aml.amount_residual), 0) ", kind=None),
                                            op=Add(),
                                            right=Name(id='operator', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Constant(value=' %s', kind=None),
                                    ),
                                    Tuple(
                                        elts=[
                                            Name(id='account_type', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='sign', ctx=Load()),
                                            Name(id='operand', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='res', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='in', kind=None),
                                            ListComp(
                                                elt=Subscript(
                                                    value=Name(id='r', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='r', ctx=Store()),
                                                        iter=Name(id='res', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
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
                    name='_credit_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='operand', annotation=None, type_comment=None),
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
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_asset_difference_search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='receivable', kind=None),
                                    Name(id='operator', ctx=Load()),
                                    Name(id='operand', ctx=Load()),
                                ],
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
                    name='_debit_search',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='operand', annotation=None, type_comment=None),
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
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_asset_difference_search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='payable', kind=None),
                                    Name(id='operator', ctx=Load()),
                                    Name(id='operand', ctx=Load()),
                                ],
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
                    name='_invoice_total',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='total_invoiced',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ids',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='all_partners_and_children', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='all_partner_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='all_partners_and_children', ctx=Load()),
                                            slice=Name(id='partner', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='active_test',
                                                            value=Constant(value=False, kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='id', kind=None),
                                                                Constant(value='child_of', kind=None),
                                                                Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
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
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='all_partner_ids', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Name(id='all_partners_and_children', ctx=Load()),
                                        slice=Name(id='partner', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Name(id='all_partner_ids', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='not in', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='draft', kind=None),
                                                    Constant(value='cancel', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='in', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Constant(value='out_refund', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='price_totals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.invoice.report', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[Constant(value='price_subtotal', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='partner_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='partner', ctx=Store()),
                                    Name(id='child_ids', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='all_partners_and_children', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='total_invoiced',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Subscript(
                                                    value=Name(id='price', ctx=Load()),
                                                    slice=Constant(value='price_subtotal', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='price', ctx=Store()),
                                                        iter=Name(id='price_totals', ctx=Load()),
                                                        ifs=[
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='price', ctx=Load()),
                                                                        slice=Constant(value='partner_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='child_ids', ctx=Load())],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_journal_item_count',
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
                        Assign(
                            targets=[Name(id='AccountMoveLine', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move.line', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='journal_item_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='AccountMoveLine', ctx=Load()),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='partner_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_has_unreconciled_entries',
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
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='active',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='is_company',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='parent_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='has_unreconciled_entries',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=' SELECT 1 FROM(\n                        SELECT\n                            p.last_time_entries_checked AS last_time_entries_checked,\n                            MAX(l.write_date) AS max_date\n                        FROM\n                            account_move_line l\n                            RIGHT JOIN account_account a ON (a.id = l.account_id)\n                            RIGHT JOIN res_partner p ON (l.partner_id = p.id)\n                        WHERE\n                            p.id = %s\n                            AND EXISTS (\n                                SELECT 1\n                                FROM account_move_line l\n                                WHERE l.account_id = a.id\n                                AND l.partner_id = p.id\n                                AND l.amount_residual > 0\n                            )\n                            AND EXISTS (\n                                SELECT 1\n                                FROM account_move_line l\n                                WHERE l.account_id = a.id\n                                AND l.partner_id = p.id\n                                AND l.amount_residual < 0\n                            )\n                        GROUP BY p.last_time_entries_checked\n                    ) as s\n                    WHERE (last_time_entries_checked IS NULL OR max_date > last_time_entries_checked)\n                ', kind=None),
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='has_unreconciled_entries',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='rowcount',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='mark_as_reconciled',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.partial.reconcile', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='write', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='last_time_entries_checked', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
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
                    name='_get_company_currency',
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
                                If(
                                    test=Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='credit', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_credit_debit_get', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Name(id='_credit_search', ctx=Load()),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Total Receivable', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Total amount this customer owes you.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='debit', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_credit_debit_get', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Name(id='_debit_search', ctx=Load()),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Total Payable', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Total amount you have to pay to this vendor.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='debit_limit', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Payable Limit', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='total_invoiced', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_invoice_total', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Total Invoiced', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='account.group_account_invoice,account.group_account_readonly', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.currency', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_get_company_currency', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Currency', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Utility field to express amount currency', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='journal_item_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_journal_item_count', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Journal Items', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_account_payable_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Account Payable', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('internal_type', '=', 'payable'), ('deprecated', '=', False), ('company_id', '=', current_company_id)]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This account will be used instead of the default one as the payable account for the current partner', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_account_receivable_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Account Receivable', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('internal_type', '=', 'receivable'), ('deprecated', '=', False), ('company_id', '=', current_company_id)]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This account will be used instead of the default one as the receivable account for the current partner', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_account_position_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.fiscal.position', kind=None)],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Fiscal Position', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', '=', current_company_id)]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The fiscal position determines the taxes/accounts used for this contact.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_payment_term_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.payment.term', kind=None)],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Customer Payment Terms', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', 'in', [current_company_id, False])]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This payment term will be used instead of the default one for sales orders and customer invoices', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='property_supplier_payment_term_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.payment.term', kind=None)],
                        keywords=[
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Vendor Payment Terms', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', 'in', [current_company_id, False])]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This payment term will be used instead of the default one for purchase orders and vendor bills', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ref_company_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.company', kind=None),
                            Constant(value='partner_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Companies that refers to partner', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='has_unreconciled_entries', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_has_unreconciled_entries', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The partner has at least one unreconciled debit and credit since last time the invoices & payments matching was performed.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='last_time_entries_checked', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Latest Invoices & Payments Matching Date', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Last time the invoices & payments matching was performed for this partner. It is set either if there\'s not at least an unreconciled debit and an unreconciled credit or if you click the "Done" button.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='invoice_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.move', kind=None),
                            Constant(value='partner_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Invoices', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contract_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.analytic.account', kind=None),
                            Constant(value='partner_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Partner Contracts', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='bank_account_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_bank_count', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Bank', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='trust', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='good', kind=None),
                                            Constant(value='Good Debtor', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='normal', kind=None),
                                            Constant(value='Normal Debtor', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='bad', kind=None),
                                            Constant(value='Bad Debtor', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Degree of trust you have in this debtor', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='normal', kind=None),
                            ),
                            keyword(
                                arg='company_dependent',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='invoice_warn', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='WARNING_MESSAGE', ctx=Load()),
                            Constant(value='Invoice', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Name(id='WARNING_HELP', ctx=Load()),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='no-message', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='invoice_warn_msg', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Message for Invoice', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='supplier_rank', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='customer_rank', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_name_search_order_by_fields',
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
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_name_search_order_by_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_search_mode', ctx=Store())],
                            value=Call(
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
                                args=[Constant(value='res_partner_search_mode', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=Name(id='partner_search_mode', ctx=Load()),
                                    ops=[In()],
                                    comparators=[
                                        Tuple(
                                            elts=[
                                                Constant(value='customer', kind=None),
                                                Constant(value='supplier', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='order_by_field', ctx=Store())],
                            value=Constant(value='COALESCE(res_partner.%s, 0) DESC,', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='partner_search_mode', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='customer', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='field', ctx=Store())],
                                    value=Constant(value='customer_rank', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='field', ctx=Store())],
                                    value=Constant(value='supplier_rank', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='order_by_field', ctx=Store())],
                            value=BinOp(
                                left=Name(id='order_by_field', ctx=Load()),
                                op=Mod(),
                                right=Name(id='field', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id='res', ctx=Load()),
                                body=BinOp(
                                    left=Constant(value='%s, %s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Name(id='res', ctx=Load()),
                                            BinOp(
                                                left=Name(id='order_by_field', ctx=Load()),
                                                op=Mod(),
                                                right=Name(id='field', ctx=Load()),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Name(id='order_by_field', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_bank_count',
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
                        Assign(
                            targets=[Name(id='bank_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner.bank', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='partner_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='partner_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapped_data', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='bank', ctx=Load()),
                                                        slice=Constant(value='partner_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='bank', ctx=Load()),
                                                    slice=Constant(value='partner_id_count', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='bank', ctx=Store()),
                                                iter=Name(id='bank_data', ctx=Load()),
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
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='bank_account_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mapped_data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_find_accounting_partner',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Find the partner for which the accounting entries will be created ', kind=None),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='partner', ctx=Load()),
                                attr='commercial_partner_id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_commercial_fields',
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
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[
                                                Name(id='ResPartner', ctx=Load()),
                                                Name(id='self', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='_commercial_fields',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Constant(value='debit_limit', kind=None),
                                        Constant(value='property_account_payable_id', kind=None),
                                        Constant(value='property_account_receivable_id', kind=None),
                                        Constant(value='property_account_position_id', kind=None),
                                        Constant(value='property_payment_term_id', kind=None),
                                        Constant(value='property_supplier_payment_term_id', kind=None),
                                        Constant(value='last_time_entries_checked', kind=None),
                                    ],
                                    ctx=Load(),
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
                FunctionDef(
                    name='action_view_partner_invoices',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='account.action_move_out_invoice_type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='domain', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='in', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Constant(value='out_refund', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='child_of', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='default_move_type', kind=None),
                                    Constant(value='move_type', kind=None),
                                    Constant(value='journal_type', kind=None),
                                    Constant(value='search_default_unpaid', kind=None),
                                ],
                                values=[
                                    Constant(value='out_invoice', kind=None),
                                    Constant(value='out_invoice', kind=None),
                                    Constant(value='sale', kind=None),
                                    Constant(value=1, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='can_edit_vat',
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
                        Expr(
                            value=Constant(value=" Can't edit `vat` if there is (non draft) issued invoices. ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='can_edit_vat', ctx=Store())],
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
                                    attr='can_edit_vat',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='can_edit_vat', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='can_edit_vat', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='has_invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
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
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='out_invoice', kind=None),
                                                            Constant(value='out_refund', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='child_of', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='commercial_partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='posted', kind=None),
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
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='can_edit_vat', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='bool', ctx=Load()),
                                            args=[Name(id='has_invoice', ctx=Load())],
                                            keywords=[],
                                        ),
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
                        Assign(
                            targets=[Name(id='search_partner_mode', ctx=Store())],
                            value=Call(
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
                                args=[Constant(value='res_partner_search_mode', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_customer', ctx=Store())],
                            value=Compare(
                                left=Name(id='search_partner_mode', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='customer', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_supplier', ctx=Store())],
                            value=Compare(
                                left=Name(id='search_partner_mode', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='supplier', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='search_partner_mode', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='vals', ctx=Store()),
                                    iter=Name(id='vals_list', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='is_customer', ctx=Load()),
                                                    Compare(
                                                        left=Constant(value='customer_rank', kind=None),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='vals', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Constant(value='customer_rank', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=1, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='is_supplier', ctx=Load()),
                                                            Compare(
                                                                left=Constant(value='supplier_rank', kind=None),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='vals', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='vals', ctx=Load()),
                                                                    slice=Constant(value='supplier_rank', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=1, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
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
                                        args=[],
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
                    name='_increase_rank',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='n', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Name(id='field', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='customer_rank', kind=None),
                                                    Constant(value='supplier_rank', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Try(
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='savepoint',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='flush',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
                                            body=[
                                                Assign(
                                                    targets=[Name(id='query', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='sql', ctx=Load()),
                                                                    attr='SQL',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='\n                        SELECT {field} FROM res_partner WHERE ID IN %(partner_ids)s FOR UPDATE NOWAIT;\n                        UPDATE res_partner SET {field} = {field} + %(n)s\n                        WHERE id IN %(partner_ids)s\n                    ', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='field',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Identifier',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='field', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='execute',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='query', ctx=Load()),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='partner_ids', kind=None),
                                                                    Constant(value='n', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='tuple', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='n', ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                For(
                                                    target=Name(id='partner', ctx=Store()),
                                                    iter=Name(id='self', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='cache',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='remove',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='partner', ctx=Load()),
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='partner', ctx=Load()),
                                                                            attr='_fields',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Name(id='field', ctx=Load()),
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
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='DatabaseError', ctx=Load()),
                                            name='e',
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='pgcode',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='55P03', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='debug',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='Another transaction already locked partner rows. Cannot update partner ranks.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Raise(
                                                            exc=Name(id='e', ctx=Load()),
                                                            cause=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
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

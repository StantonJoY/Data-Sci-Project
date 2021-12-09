Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.l10n_it_edi.tools.remove_signature',
            names=[alias(name='remove_signature', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[
                alias(name='OR', asname=None),
                alias(name='AND', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
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
            targets=[Name(id='DEFAULT_FACTUR_ITALIAN_DATE_FORMAT', ctx=Store())],
            value=Constant(value='%Y-%m-%d', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='AccountEdiFormat',
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
                    value=Constant(value='account.edi.format', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_l10n_it_edi_generate_electronic_invoice_filename',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns a name conform to the Fattura pa Specifications:\n           See ES documentation 2.2\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='a', ctx=Store())],
                            value=Constant(value='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='n', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='progressive_number', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        While(
                            test=Name(id='n', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='n', ctx=Store()),
                                                Name(id='m', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='divmod', ctx=Load()),
                                        args=[
                                            Name(id='n', ctx=Load()),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='a', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='progressive_number', ctx=Store())],
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='a', ctx=Load()),
                                            slice=Name(id='m', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Name(id='progressive_number', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%(country_code)s%(codice)s_%(progressive_number)s.xml', kind=None),
                                op=Mod(),
                                right=Dict(
                                    keys=[
                                        Constant(value='country_code', kind=None),
                                        Constant(value='codice', kind=None),
                                        Constant(value='progressive_number', kind=None),
                                    ],
                                    values=[
                                        Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='l10n_it_codice_fiscale',
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
                                        Call(
                                            func=Attribute(
                                                value=Name(id='progressive_number', ctx=Load()),
                                                attr='zfill',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=5, kind=None)],
                                            keywords=[],
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
                FunctionDef(
                    name='_l10n_it_edi_check_invoice_configuration',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='errors', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='seller', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='buyer', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='commercial_partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='seller', ctx=Load()),
                                    attr='country_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a country', kind=None),
                                                    Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='display_name',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='seller', ctx=Load()),
                                    attr='vat',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a VAT number', kind=None),
                                                    Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='display_name',
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
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='seller', ctx=Load()),
                                                    attr='vat',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=30, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='errors', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='The maximum length for VAT number is 30. %s have a VAT number too long: %s.', kind=None),
                                                            Attribute(
                                                                value=Name(id='seller', ctx=Load()),
                                                                attr='display_name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='seller', ctx=Load()),
                                                                attr='vat',
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
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='seller', ctx=Load()),
                                    attr='l10n_it_codice_fiscale',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a codice fiscale number', kind=None),
                                                    Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='display_name',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='seller', ctx=Load()),
                                    attr='l10n_it_tax_system',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="The seller's company must have a tax system.", kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                                        operand=Attribute(
                                            value=Name(id='seller', ctx=Load()),
                                            attr='street',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='seller', ctx=Load()),
                                            attr='street2',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a street.', kind=None),
                                                    Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='display_name',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='seller', ctx=Load()),
                                    attr='zip',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a post code.', kind=None),
                                                    Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='display_name',
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
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='seller', ctx=Load()),
                                                            attr='zip',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=5, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='IT', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='errors', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='%s must have a post code of length 5.', kind=None),
                                                            Attribute(
                                                                value=Name(id='seller', ctx=Load()),
                                                                attr='display_name',
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
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='seller', ctx=Load()),
                                    attr='city',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a city.', kind=None),
                                                    Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='display_name',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='seller', ctx=Load()),
                                    attr='country_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a country.', kind=None),
                                                    Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='display_name',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='seller', ctx=Load()),
                                        attr='l10n_it_has_tax_representative',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='seller', ctx=Load()),
                                                attr='l10n_it_tax_representative_partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='vat',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Tax representative partner %s of %s must have a tax number.', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='seller', ctx=Load()),
                                                            attr='l10n_it_tax_representative_partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='display_name',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='buyer', ctx=Load()),
                                            attr='vat',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='buyer', ctx=Load()),
                                            attr='l10n_it_codice_fiscale',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='buyer', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='IT', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The buyer, %s, or his company must have either a VAT number either a tax code (Codice Fiscale).', kind=None),
                                                    Attribute(
                                                        value=Name(id='buyer', ctx=Load()),
                                                        attr='display_name',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='buyer', ctx=Load()),
                                            attr='street',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='buyer', ctx=Load()),
                                            attr='street2',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a street.', kind=None),
                                                    Attribute(
                                                        value=Name(id='buyer', ctx=Load()),
                                                        attr='display_name',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='buyer', ctx=Load()),
                                    attr='zip',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a post code.', kind=None),
                                                    Attribute(
                                                        value=Name(id='buyer', ctx=Load()),
                                                        attr='display_name',
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
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='buyer', ctx=Load()),
                                                            attr='zip',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=5, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='buyer', ctx=Load()),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='IT', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='errors', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='%s must have a post code of length 5.', kind=None),
                                                            Attribute(
                                                                value=Name(id='buyer', ctx=Load()),
                                                                attr='display_name',
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
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='buyer', ctx=Load()),
                                    attr='city',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a city.', kind=None),
                                                    Attribute(
                                                        value=Name(id='buyer', ctx=Load()),
                                                        attr='display_name',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='buyer', ctx=Load()),
                                    attr='country_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s must have a country.', kind=None),
                                                    Attribute(
                                                        value=Name(id='buyer', ctx=Load()),
                                                        attr='display_name',
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
                        For(
                            target=Name(id='invoice_line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='invoice_line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='invoice_line', ctx=Load()),
                                                    attr='display_type',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='invoice_line', ctx=Load()),
                                                            attr='tax_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='You must select one and only one tax by line.', kind=None)],
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
                        For(
                            target=Name(id='tax_line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='tax_line_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tax_line', ctx=Load()),
                                                        attr='tax_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='l10n_it_kind_exoneration',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='tax_line', ctx=Load()),
                                                        attr='tax_line_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='errors', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='%s has an amount of 0.0, you must indicate the kind of exoneration.', kind=None),
                                                            Attribute(
                                                                value=Name(id='tax_line', ctx=Load()),
                                                                attr='name',
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='partner_bank_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='errors', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The seller must have a bank account.', kind=None)],
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
                            value=Name(id='errors', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_embedding_to_invoice_pdf_needed',
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
                        Return(
                            value=IfExp(
                                test=Compare(
                                    left=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value='fattura_pa', kind=None)],
                                ),
                                body=Constant(value=True, kind=None),
                                orelse=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='_is_embedding_to_invoice_pdf_needed',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_compatible_with_journal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='journal', annotation=None, type_comment=None),
                        ],
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='fattura_pa', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_is_compatible_with_journal',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='journal', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='journal', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='sale', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='journal', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='IT', kind=None)],
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
                    name='_l10n_it_edi_is_required_for_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Is the edi required for this invoice based on the method (here: PEC mail)\n            Deprecated: in future release PEC mail will be removed.\n            TO OVERRIDE\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='l10n_it_send_state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='sent', kind=None),
                                                    Constant(value='delivered', kind=None),
                                                    Constant(value='delivered_accepted', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='IT', kind=None)],
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
                    name='_is_required_for_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='fattura_pa', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_is_required_for_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoice', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_l10n_it_edi_is_required_for_invoice',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post_fattura_pa',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoices', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Name(id='invoices', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='l10n_it_send_state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='other', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='_check_before_xml_exporting',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='l10n_it_einvoice_id',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='l10n_it_send_state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='invalid', kind=None),
                                                    Constant(value='to_send', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="You can't regenerate an E-Invoice when the first one is sent and there are no errors", kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='l10n_it_einvoice_id',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='l10n_it_einvoice_id',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='invoice_generate_xml',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
                                                        attr='commercial_partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='l10n_it_pa_index',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=6, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Invoices for PA are not managed by Odoo, you can download the document and send it on your own.', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='l10n_it_send_state',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='to_send', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='attachment', kind=None),
                                ops=[In()],
                                comparators=[Name(id='res', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='success', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[Name(id='invoice', ctx=Load())],
                                values=[Name(id='res', ctx=Load())],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post_invoice_edi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoices', annotation=None, type_comment=None),
                            arg(arg='test_mode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
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
                            targets=[Name(id='edi_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_post_invoice_edi',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoices', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='fattura_pa', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='edi_result', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_post_fattura_pa',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoices', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_filename_is_fattura_pa',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
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
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='([A-Z]{2}[A-Za-z0-9]{2,28}_[A-Za-z0-9]{0,5}.(xml.p7m|xml))', kind=None),
                                    Name(id='filename', ctx=Load()),
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
                    name='_is_fattura_pa',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='fattura_pa', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_filename_is_fattura_pa',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='filename', ctx=Load())],
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
                    name='_create_invoice_from_xml_tree',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                        ],
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_fattura_pa',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_import_fattura_pa',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tree', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move', kind=None),
                                                ctx=Load(),
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
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_create_invoice_from_xml_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
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
                    name='_update_invoice_from_xml_tree',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_fattura_pa',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='tree', ctx=Load()),
                                                        attr='xpath',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='//FatturaElettronicaBody', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Constant(value='The attachment contains multiple invoices, this invoice was not updated from it.', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='message_type',
                                                        value=Constant(value='comment', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='subtype_xmlid',
                                                        value=Constant(value='mail.mt_note', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='author_id',
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
                                                                args=[Constant(value='base.partner_root', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_import_fattura_pa',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='tree', ctx=Load()),
                                                    Name(id='invoice', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
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
                                    attr='_update_invoice_from_xml_tree',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='tree', ctx=Load()),
                                    Name(id='invoice', ctx=Load()),
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
                    name='_decode_p7m_to_xml',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='decoded_content', ctx=Store())],
                            value=Call(
                                func=Name(id='remove_signature', ctx=Load()),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='decoded_content', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='parser', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='XMLParser',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='recover',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='xml_tree', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='decoded_content', ctx=Load()),
                                            Name(id='parser', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Error when converting the xml content to etree: %s', kind=None),
                                                    Name(id='e', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value=None, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='xml_tree', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='xml_tree', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='xml_tree', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_invoice_from_binary',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                        ],
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
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='extension', ctx=Load()),
                                        attr='lower',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='.xml.p7m', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='decoded_content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_decode_p7m_to_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='filename', ctx=Load()),
                                            Name(id='content', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='decoded_content', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_is_fattura_pa',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='filename', ctx=Load()),
                                                    Name(id='decoded_content', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_import_fattura_pa',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='decoded_content', ctx=Load()),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.move', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_create_invoice_from_binary',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                    Name(id='extension', ctx=Load()),
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
                    name='_update_invoice_from_binary',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
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
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='extension', ctx=Load()),
                                        attr='lower',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='.xml.p7m', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='decoded_content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_decode_p7m_to_xml',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='filename', ctx=Load()),
                                            Name(id='content', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='decoded_content', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_is_fattura_pa',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='filename', ctx=Load()),
                                                    Name(id='decoded_content', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_import_fattura_pa',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='decoded_content', ctx=Load()),
                                                    Name(id='invoice', ctx=Load()),
                                                ],
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_update_invoice_from_binary',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='filename', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                    Name(id='extension', ctx=Load()),
                                    Name(id='invoice', ctx=Load()),
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
                    name='_import_fattura_pa',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Decodes a fattura_pa invoice into an invoice.\n\n        :param tree:    the fattura_pa tree to decode.\n        :param invoice: the invoice to update or an empty recordset.\n        :returns:       the invoice where the fattura_pa data was imported.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='invoices', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.move', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_run', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='body_tree', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//FatturaElettronicaBody', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='first_run', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='invoice', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='invoice', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='first_run', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//CessionarioCommittente//IdCodice', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='elements', ctx=Load()),
                                            Call(
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
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='vat', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='elements', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='text',
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
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='company', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='//CessionarioCommittente//CodiceFiscale', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='company', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='elements', ctx=Load()),
                                                    Call(
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
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='l10n_it_codice_fiscale', kind=None),
                                                                            Constant(value='ilike', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Name(id='elements', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='text',
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
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='company', ctx=Load()),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='No company found with VAT or Codice Fiscale like %r.', kind=None),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='elements', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='//DatiGeneraliDocumento/TipoDocumento', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move_type', ctx=Store())],
                                    value=Constant(value='in_invoice', kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='elements', ctx=Load()),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='elements', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='elements', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='TD04', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='move_type', ctx=Store())],
                                            value=Constant(value='in_refund', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='elements', ctx=Load()),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='elements', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='elements', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='TD01', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Document type not managed: %s. Invoice type is set by default.', kind=None),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='elements', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='invoice_ctx', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='with_company',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='company', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_move_type',
                                                value=Name(id='move_type', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='account_predictive_bills_disable_prediction',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='Form', ctx=Load()),
                                                args=[Name(id='invoice_ctx', ctx=Load())],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='invoice_form', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='message_to_log', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='//CedentePrestatore//IdCodice', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='partner', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='elements', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.partner', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='&', kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='vat', kind=None),
                                                                            Constant(value='ilike', kind=None),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Name(id='elements', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='text',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='|', kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='company_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='company', ctx=Load()),
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
                                                                            Constant(value=False, kind=None),
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
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='partner', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='elements', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tree', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='//CedentePrestatore//CodiceFiscale', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='elements', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='codice', ctx=Store())],
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='elements', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='domains', ctx=Store())],
                                                            value=List(
                                                                elts=[
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='l10n_it_codice_fiscale', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Name(id='codice', ctx=Load()),
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
                                                        If(
                                                            test=Call(
                                                                func=Attribute(
                                                                    value=Name(id='re', ctx=Load()),
                                                                    attr='match',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='^[0-9]{11}$', kind=None),
                                                                    Name(id='codice', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='domains', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='l10n_it_codice_fiscale', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            BinOp(
                                                                                                left=Constant(value='IT', kind=None),
                                                                                                op=Add(),
                                                                                                right=Name(id='codice', ctx=Load()),
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
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='re', ctx=Load()),
                                                                            attr='match',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='^IT[0-9]{11}$', kind=None),
                                                                            Name(id='codice', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='domains', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Constant(value='l10n_it_codice_fiscale', kind=None),
                                                                                                    Constant(value='=', kind=None),
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Subscript(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                    attr='env',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                slice=Constant(value='res.partner', kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='_l10n_it_normalize_codice_fiscale',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[Name(id='codice', ctx=Load())],
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
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='partner', ctx=Store())],
                                                            value=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='elements', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='res.partner', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='search',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='AND', ctx=Load()),
                                                                                args=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Call(
                                                                                                func=Name(id='OR', ctx=Load()),
                                                                                                args=[Name(id='domains', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            Call(
                                                                                                func=Name(id='OR', ctx=Load()),
                                                                                                args=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Tuple(
                                                                                                                        elts=[
                                                                                                                            Constant(value='company_id', kind=None),
                                                                                                                            Constant(value='=', kind=None),
                                                                                                                            Attribute(
                                                                                                                                value=Name(id='company', ctx=Load()),
                                                                                                                                attr='id',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                ],
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Tuple(
                                                                                                                        elts=[
                                                                                                                            Constant(value='company_id', kind=None),
                                                                                                                            Constant(value='=', kind=None),
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
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='limit',
                                                                                value=Constant(value=1, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='partner', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='elements', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tree', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='//DatiTrasmissione//Email', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='partner', ctx=Store())],
                                                    value=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='elements', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='res.partner', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='search',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='&', kind=None),
                                                                            Constant(value='|', kind=None),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='email', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='elements', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='text',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='l10n_it_pec_email', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='elements', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='text',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='|', kind=None),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='company_id', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='company', ctx=Load()),
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
                                                                                    Constant(value=False, kind=None),
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
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='partner', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='partner', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='message_to_log', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='%s<br/>%s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Vendor not found, useful informations from XML file:', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='invoice', ctx=Load()),
                                                                                attr='_compose_info_message',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Name(id='tree', ctx=Load()),
                                                                                Constant(value='.//CedentePrestatore', kind=None),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='//ProgressivoInvio', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='elements', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='payment_reference',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='elements', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//DatiGeneraliDocumento//Numero', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='elements', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='ref',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='elements', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//DatiGeneraliDocumento/Divisa', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='elements', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='currency_str', ctx=Store())],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='elements', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='currency', ctx=Store())],
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
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='base.%s', kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='currency_str', ctx=Load()),
                                                                        attr='upper',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='raise_if_not_found',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='currency', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[
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
                                                                        attr='currency_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='currency', ctx=Load()),
                                                                attr='active',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_form', ctx=Load()),
                                                                    attr='currency_id',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='currency', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//DatiGeneraliDocumento/Data', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='elements', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='date_str', ctx=Store())],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='elements', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='date_obj', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='strptime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='date_str', ctx=Load()),
                                                            Name(id='DEFAULT_FACTUR_ITALIAN_DATE_FORMAT', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='invoice_date',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='date_obj', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//DatiGeneraliDocumento/DatiBollo/ImportoBollo', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='elements', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='l10n_it_stamp_duty',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='float', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='elements', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='text',
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
                                        Assign(
                                            targets=[Name(id='discount_list', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='percentage_global_discount', ctx=Store())],
                                            value=Constant(value=1.0, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='discount_elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//DatiGeneraliDocumento/ScontoMaggiorazione', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='total_discount_amount', ctx=Store())],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='discount_elements', ctx=Load()),
                                            body=[
                                                For(
                                                    target=Name(id='discount_element', ctx=Store()),
                                                    iter=Name(id='discount_elements', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='discount_line', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='discount_element', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.//Tipo', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='discount_sign', ctx=Store())],
                                                            value=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='discount_line', ctx=Load()),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='discount_line', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='text',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='SC', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='discount_sign', ctx=Store())],
                                                                    value=Constant(value=1, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='discount_percentage', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='discount_element', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.//Percentuale', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='discount_percentage', ctx=Load()),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='discount_percentage', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='percentage_global_discount', ctx=Store()),
                                                                    op=Mult(),
                                                                    value=BinOp(
                                                                        left=Constant(value=1, kind=None),
                                                                        op=Sub(),
                                                                        right=BinOp(
                                                                            left=BinOp(
                                                                                left=Call(
                                                                                    func=Name(id='float', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Subscript(
                                                                                                value=Name(id='discount_percentage', ctx=Load()),
                                                                                                slice=Constant(value=0, kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='text',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Div(),
                                                                                right=Constant(value=100, kind=None),
                                                                            ),
                                                                            op=Mult(),
                                                                            right=Name(id='discount_sign', ctx=Load()),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='discount_amount_text', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='discount_element', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.//Importo', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='discount_amount_text', ctx=Load()),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='discount_amount_text', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='discount_amount', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=BinOp(
                                                                            left=Call(
                                                                                func=Name(id='float', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='discount_amount_text', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='text',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            op=Mult(),
                                                                            right=Name(id='discount_sign', ctx=Load()),
                                                                        ),
                                                                        op=Mult(),
                                                                        right=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Constant(value=1, kind=None),
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='discount', ctx=Store())],
                                                                    value=Dict(keys=[], values=[]),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='discount', ctx=Load()),
                                                                            slice=Constant(value='seq', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value=0, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='discount_amount', ctx=Load()),
                                                                        ops=[Lt()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='discount', ctx=Load()),
                                                                                    slice=Constant(value='name', kind=None),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='GLOBAL DISCOUNT', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='discount', ctx=Load()),
                                                                                    slice=Constant(value='name', kind=None),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='GLOBAL EXTRA CHARGE', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='discount', ctx=Load()),
                                                                            slice=Constant(value='amount', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='discount_amount', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='discount', ctx=Load()),
                                                                            slice=Constant(value='tax', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=List(elts=[], ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='discount_list', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='discount', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//DatiGeneraliDocumento//Causale', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='element', ctx=Store()),
                                            iter=Name(id='elements', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='narration',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Constant(value='%s%s<br/>', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='invoice_form', ctx=Load()),
                                                                            attr='narration',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value='', kind=None),
                                                                    ],
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='text',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='document_type', ctx=Store()),
                                            iter=List(
                                                elts=[
                                                    Constant(value='DatiOrdineAcquisto', kind=None),
                                                    Constant(value='DatiContratto', kind=None),
                                                    Constant(value='DatiConvenzione', kind=None),
                                                    Constant(value='DatiRicezione', kind=None),
                                                    Constant(value='DatiFattureCollegate', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='elements', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='body_tree', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='.//DatiGenerali/', kind=None),
                                                                op=Add(),
                                                                right=Name(id='document_type', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='elements', ctx=Load()),
                                                    body=[
                                                        For(
                                                            target=Name(id='element', ctx=Store()),
                                                            iter=Name(id='elements', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='message_to_log', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Constant(value='%s %s<br/>%s', kind=None),
                                                                                op=Mod(),
                                                                                right=Tuple(
                                                                                    elts=[
                                                                                        Name(id='document_type', ctx=Load()),
                                                                                        Call(
                                                                                            func=Name(id='_', ctx=Load()),
                                                                                            args=[Constant(value='from XML file:', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='invoice', ctx=Load()),
                                                                                                attr='_compose_info_message',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Name(id='element', ctx=Load()),
                                                                                                Constant(value='.', kind=None),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                    ],
                                                                                    ctx=Load(),
                                                                                ),
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
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//DatiGenerali/DatiDDT', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='elements', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='message_to_log', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='%s<br/>%s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Transport informations from XML file:', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='invoice', ctx=Load()),
                                                                                attr='_compose_info_message',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Name(id='body_tree', ctx=Load()),
                                                                                Constant(value='.//DatiGenerali/DatiDDT', kind=None),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//DatiPagamento/DettaglioPagamento/DataScadenzaPagamento', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='elements', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='date_str', ctx=Store())],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='elements', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='date_obj', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='strptime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='date_str', ctx=Load()),
                                                            Name(id='DEFAULT_FACTUR_ITALIAN_DATE_FORMAT', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='invoice_form', ctx=Load()),
                                                            attr='invoice_date_due',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='date_obj', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//ImportoPagamento', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='amount_total_import', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='element', ctx=Store()),
                                            iter=Name(id='elements', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='amount_total_import', ctx=Store()),
                                                    op=Add(),
                                                    value=Call(
                                                        func=Name(id='float', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='element', ctx=Load()),
                                                                attr='text',
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
                                        If(
                                            test=Name(id='amount_total_import', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='message_to_log', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Total amount from the XML File: %s', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Name(id='amount_total_import', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='invoice_form', ctx=Load()),
                                                    attr='move_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='out_invoice', kind=None),
                                                            Constant(value='in_refund', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='elements', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='body_tree', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='.//DatiPagamento/DettaglioPagamento/IBAN', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='elements', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='invoice_form', ctx=Load()),
                                                                        attr='partner_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='invoice_form', ctx=Load()),
                                                                            attr='partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='commercial_partner_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='bank', ctx=Store())],
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
                                                                            attr='search',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='acc_number', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Name(id='elements', ctx=Load()),
                                                                                                    slice=Constant(value=0, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='text',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='partner_id.id', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='invoice_form', ctx=Load()),
                                                                                                        attr='partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='commercial_partner_id',
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
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='bank', ctx=Store())],
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
                                                                            attr='search',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='acc_number', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Name(id='elements', ctx=Load()),
                                                                                                    slice=Constant(value=0, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='text',
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
                                                        ),
                                                        If(
                                                            test=Name(id='bank', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='invoice_form', ctx=Load()),
                                                                            attr='partner_bank_id',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='bank', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='message_to_log', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Constant(value='%s<br/>%s', kind=None),
                                                                                op=Mod(),
                                                                                right=Tuple(
                                                                                    elts=[
                                                                                        Call(
                                                                                            func=Name(id='_', ctx=Load()),
                                                                                            args=[Constant(value='Bank account not found, useful informations from XML file:', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='invoice', ctx=Load()),
                                                                                                attr='_compose_multi_info_message',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[
                                                                                                Name(id='body_tree', ctx=Load()),
                                                                                                List(
                                                                                                    elts=[
                                                                                                        Constant(value='.//DatiPagamento//Beneficiario', kind=None),
                                                                                                        Constant(value='.//DatiPagamento//IstitutoFinanziario', kind=None),
                                                                                                        Constant(value='.//DatiPagamento//IBAN', kind=None),
                                                                                                        Constant(value='.//DatiPagamento//ABI', kind=None),
                                                                                                        Constant(value='.//DatiPagamento//CAB', kind=None),
                                                                                                        Constant(value='.//DatiPagamento//BIC', kind=None),
                                                                                                        Constant(value='.//DatiPagamento//ModalitaPagamento', kind=None),
                                                                                                    ],
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                    ],
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='elements', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='body_tree', ctx=Load()),
                                                            attr='xpath',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='.//DatiPagamento/DettaglioPagamento', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='elements', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='message_to_log', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='%s<br/>%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Call(
                                                                                    func=Name(id='_', ctx=Load()),
                                                                                    args=[Constant(value='Bank account not found, useful informations from XML file:', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='invoice', ctx=Load()),
                                                                                        attr='_compose_info_message',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Name(id='body_tree', ctx=Load()),
                                                                                        Constant(value='.//DatiPagamento', kind=None),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='elements', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='body_tree', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='.//DettaglioLinee', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='elements', ctx=Load()),
                                            body=[
                                                For(
                                                    target=Name(id='element', ctx=Store()),
                                                    iter=Name(id='elements', ctx=Load()),
                                                    body=[
                                                        With(
                                                            items=[
                                                                withitem(
                                                                    context_expr=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='invoice_form', ctx=Load()),
                                                                                attr='invoice_line_ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='new',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    optional_vars=Name(id='invoice_line_form', ctx=Store()),
                                                                ),
                                                            ],
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='line_elements', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//NumeroLinea', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='line_elements', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                    attr='sequence',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=BinOp(
                                                                                left=Call(
                                                                                    func=Name(id='int', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Subscript(
                                                                                                value=Name(id='line_elements', ctx=Load()),
                                                                                                slice=Constant(value=0, kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='text',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Mult(),
                                                                                right=Constant(value=2, kind=None),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='line_elements', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//Descrizione', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='line_elements', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                    attr='name',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Constant(value=' ', kind=None),
                                                                                    attr='join',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Name(id='line_elements', ctx=Load()),
                                                                                                    slice=Constant(value=0, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='text',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='split',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='elements_code', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//CodiceArticolo', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='elements_code', ctx=Load()),
                                                                    body=[
                                                                        For(
                                                                            target=Name(id='element_code', ctx=Store()),
                                                                            iter=Name(id='elements_code', ctx=Load()),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='type_code', ctx=Store())],
                                                                                    value=Subscript(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='element_code', ctx=Load()),
                                                                                                attr='xpath',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='.//CodiceTipo', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='code', ctx=Store())],
                                                                                    value=Subscript(
                                                                                        value=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='element_code', ctx=Load()),
                                                                                                attr='xpath',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='.//CodiceValore', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='type_code', ctx=Load()),
                                                                                            attr='text',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='EAN', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='product', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='env',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value='product.product', kind=None),
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
                                                                                                                    Constant(value='barcode', kind=None),
                                                                                                                    Constant(value='=', kind=None),
                                                                                                                    Attribute(
                                                                                                                        value=Name(id='code', ctx=Load()),
                                                                                                                        attr='text',
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
                                                                                        If(
                                                                                            test=Name(id='product', ctx=Load()),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[
                                                                                                        Attribute(
                                                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                                                            attr='product_id',
                                                                                                            ctx=Store(),
                                                                                                        ),
                                                                                                    ],
                                                                                                    value=Name(id='product', ctx=Load()),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                Break(),
                                                                                            ],
                                                                                            orelse=[],
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                ),
                                                                                If(
                                                                                    test=Name(id='partner', ctx=Load()),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='product_supplier', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='env',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value='product.supplierinfo', kind=None),
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
                                                                                                                    Attribute(
                                                                                                                        value=Name(id='partner', ctx=Load()),
                                                                                                                        attr='id',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                ],
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Constant(value='product_code', kind=None),
                                                                                                                    Constant(value='=', kind=None),
                                                                                                                    Attribute(
                                                                                                                        value=Name(id='code', ctx=Load()),
                                                                                                                        attr='text',
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
                                                                                        If(
                                                                                            test=BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    Name(id='product_supplier', ctx=Load()),
                                                                                                    Attribute(
                                                                                                        value=Name(id='product_supplier', ctx=Load()),
                                                                                                        attr='product_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[
                                                                                                        Attribute(
                                                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                                                            attr='product_id',
                                                                                                            ctx=Store(),
                                                                                                        ),
                                                                                                    ],
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='product_supplier', ctx=Load()),
                                                                                                        attr='product_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                Break(),
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
                                                                        If(
                                                                            test=UnaryOp(
                                                                                op=Not(),
                                                                                operand=Attribute(
                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                    attr='product_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            body=[
                                                                                For(
                                                                                    target=Name(id='element_code', ctx=Store()),
                                                                                    iter=Name(id='elements_code', ctx=Load()),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='code', ctx=Store())],
                                                                                            value=Subscript(
                                                                                                value=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='element_code', ctx=Load()),
                                                                                                        attr='xpath',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[Constant(value='.//CodiceValore', kind=None)],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                slice=Constant(value=0, kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                        Assign(
                                                                                            targets=[Name(id='product', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='env',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value='product.product', kind=None),
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
                                                                                                                    Constant(value='default_code', kind=None),
                                                                                                                    Constant(value='=', kind=None),
                                                                                                                    Attribute(
                                                                                                                        value=Name(id='code', ctx=Load()),
                                                                                                                        attr='text',
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
                                                                                        If(
                                                                                            test=Name(id='product', ctx=Load()),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[
                                                                                                        Attribute(
                                                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                                                            attr='product_id',
                                                                                                            ctx=Store(),
                                                                                                        ),
                                                                                                    ],
                                                                                                    value=Name(id='product', ctx=Load()),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                Break(),
                                                                                            ],
                                                                                            orelse=[],
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='line_elements', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//PrezzoUnitario', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='line_elements', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                    attr='price_unit',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Name(id='float', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='line_elements', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='text',
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
                                                                Assign(
                                                                    targets=[Name(id='line_elements', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//Quantita', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='line_elements', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                    attr='quantity',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Name(id='float', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='line_elements', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='text',
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
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                    attr='quantity',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value=1, kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='tax_element', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//AliquotaIVA', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='natura_element', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//Natura', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='invoice_line_form', ctx=Load()),
                                                                                attr='tax_ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='clear',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='tax_element', ctx=Load()),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Name(id='tax_element', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='text',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='percentage', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='float', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='tax_element', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='text',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Name(id='natura_element', ctx=Load()),
                                                                                    Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='natura_element', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='text',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='l10n_it_kind_exoneration', ctx=Store())],
                                                                                    value=Attribute(
                                                                                        value=Subscript(
                                                                                            value=Name(id='natura_element', ctx=Load()),
                                                                                            slice=Constant(value=0, kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='text',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='tax', ctx=Store())],
                                                                                    value=Call(
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
                                                                                                            Constant(value='company_id', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Attribute(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='invoice_form', ctx=Load()),
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
                                                                                                            Constant(value='amount_type', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Constant(value='percent', kind=None),
                                                                                                        ],
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='type_tax_use', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Constant(value='purchase', kind=None),
                                                                                                        ],
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='amount', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Name(id='percentage', ctx=Load()),
                                                                                                        ],
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='l10n_it_kind_exoneration', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Name(id='l10n_it_kind_exoneration', ctx=Load()),
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
                                                                            orelse=[
                                                                                Assign(
                                                                                    targets=[Name(id='tax', ctx=Store())],
                                                                                    value=Call(
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
                                                                                                            Constant(value='company_id', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Attribute(
                                                                                                                value=Attribute(
                                                                                                                    value=Name(id='invoice_form', ctx=Load()),
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
                                                                                                            Constant(value='amount_type', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Constant(value='percent', kind=None),
                                                                                                        ],
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='type_tax_use', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Constant(value='purchase', kind=None),
                                                                                                        ],
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='amount', kind=None),
                                                                                                            Constant(value='=', kind=None),
                                                                                                            Name(id='percentage', ctx=Load()),
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
                                                                                Assign(
                                                                                    targets=[Name(id='l10n_it_kind_exoneration', ctx=Store())],
                                                                                    value=Constant(value='', kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        If(
                                                                            test=Name(id='tax', ctx=Load()),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='invoice_line_form', ctx=Load()),
                                                                                                attr='tax_ids',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='add',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='tax', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Name(id='l10n_it_kind_exoneration', ctx=Load()),
                                                                                    body=[
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='message_to_log', ctx=Load()),
                                                                                                    attr='append',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    BinOp(
                                                                                                        left=Call(
                                                                                                            func=Name(id='_', ctx=Load()),
                                                                                                            args=[Constant(value='Tax not found with percentage: %s and exoneration %s for the article: %s', kind=None)],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                        op=Mod(),
                                                                                                        right=Tuple(
                                                                                                            elts=[
                                                                                                                Name(id='percentage', ctx=Load()),
                                                                                                                Name(id='l10n_it_kind_exoneration', ctx=Load()),
                                                                                                                Attribute(
                                                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                                                    attr='name',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                            ],
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='message_to_log', ctx=Load()),
                                                                                                    attr='append',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    BinOp(
                                                                                                        left=Call(
                                                                                                            func=Name(id='_', ctx=Load()),
                                                                                                            args=[Constant(value='Tax not found with percentage: %s for the article: %s', kind=None)],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                        op=Mod(),
                                                                                                        right=Tuple(
                                                                                                            elts=[
                                                                                                                Name(id='percentage', ctx=Load()),
                                                                                                                Attribute(
                                                                                                                    value=Name(id='invoice_line_form', ctx=Load()),
                                                                                                                    attr='name',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                            ],
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='line_elements', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//ScontoMaggiorazione', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='total_discount_amount', ctx=Store())],
                                                                    value=Constant(value=0.0, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='total_discount_percentage', ctx=Store())],
                                                                    value=Name(id='percentage_global_discount', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='line_elements', ctx=Load()),
                                                                    body=[
                                                                        For(
                                                                            target=Name(id='line_element', ctx=Store()),
                                                                            iter=Name(id='line_elements', ctx=Load()),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='discount_line', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='line_element', ctx=Load()),
                                                                                            attr='xpath',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='.//Tipo', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='discount_sign', ctx=Store())],
                                                                                    value=UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Constant(value=1, kind=None),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Name(id='discount_line', ctx=Load()),
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Name(id='discount_line', ctx=Load()),
                                                                                                        slice=Constant(value=0, kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='text',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='SC', kind=None)],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='discount_sign', ctx=Store())],
                                                                                            value=Constant(value=1, kind=None),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='discount_percentage', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='line_element', ctx=Load()),
                                                                                            attr='xpath',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='.//Percentuale', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Name(id='discount_percentage', ctx=Load()),
                                                                                            Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Name(id='discount_percentage', ctx=Load()),
                                                                                                    slice=Constant(value=0, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='text',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='pourcentage_actual', ctx=Store())],
                                                                                            value=BinOp(
                                                                                                left=Constant(value=1, kind=None),
                                                                                                op=Sub(),
                                                                                                right=BinOp(
                                                                                                    left=BinOp(
                                                                                                        left=Call(
                                                                                                            func=Name(id='float', ctx=Load()),
                                                                                                            args=[
                                                                                                                Attribute(
                                                                                                                    value=Subscript(
                                                                                                                        value=Name(id='discount_percentage', ctx=Load()),
                                                                                                                        slice=Constant(value=0, kind=None),
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    attr='text',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                            ],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                        op=Div(),
                                                                                                        right=Constant(value=100, kind=None),
                                                                                                    ),
                                                                                                    op=Mult(),
                                                                                                    right=Name(id='discount_sign', ctx=Load()),
                                                                                                ),
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                        AugAssign(
                                                                                            target=Name(id='total_discount_percentage', ctx=Store()),
                                                                                            op=Mult(),
                                                                                            value=Name(id='pourcentage_actual', ctx=Load()),
                                                                                        ),
                                                                                        AugAssign(
                                                                                            target=Name(id='total_discount_amount', ctx=Store()),
                                                                                            op=Mult(),
                                                                                            value=Name(id='pourcentage_actual', ctx=Load()),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='discount_amount', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='line_element', ctx=Load()),
                                                                                            attr='xpath',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='.//Importo', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Name(id='discount_amount', ctx=Load()),
                                                                                            Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Name(id='discount_amount', ctx=Load()),
                                                                                                    slice=Constant(value=0, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='text',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        AugAssign(
                                                                                            target=Name(id='total_discount_amount', ctx=Store()),
                                                                                            op=Add(),
                                                                                            value=BinOp(
                                                                                                left=BinOp(
                                                                                                    left=Call(
                                                                                                        func=Name(id='float', ctx=Load()),
                                                                                                        args=[
                                                                                                            Attribute(
                                                                                                                value=Subscript(
                                                                                                                    value=Name(id='discount_amount', ctx=Load()),
                                                                                                                    slice=Constant(value=0, kind=None),
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                attr='text',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    op=Mult(),
                                                                                                    right=Name(id='discount_sign', ctx=Load()),
                                                                                                ),
                                                                                                op=Mult(),
                                                                                                right=UnaryOp(
                                                                                                    op=USub(),
                                                                                                    operand=Constant(value=1, kind=None),
                                                                                                ),
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                            type_comment=None,
                                                                        ),
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='total_discount_amount', ctx=Load()),
                                                                                ops=[NotEq()],
                                                                                comparators=[Constant(value=0, kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='discount', ctx=Store())],
                                                                                    value=Dict(keys=[], values=[]),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[
                                                                                        Subscript(
                                                                                            value=Name(id='discount', ctx=Load()),
                                                                                            slice=Constant(value='seq', kind=None),
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                    ],
                                                                                    value=BinOp(
                                                                                        left=Attribute(
                                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                                            attr='sequence',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Constant(value=1, kind=None),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Name(id='total_discount_amount', ctx=Load()),
                                                                                        ops=[Lt()],
                                                                                        comparators=[Constant(value=0, kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[
                                                                                                Subscript(
                                                                                                    value=Name(id='discount', ctx=Load()),
                                                                                                    slice=Constant(value='name', kind=None),
                                                                                                    ctx=Store(),
                                                                                                ),
                                                                                            ],
                                                                                            value=Call(
                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                args=[
                                                                                                    Constant(value='DISCOUNT: %s', kind=None),
                                                                                                    Attribute(
                                                                                                        value=Name(id='invoice_line_form', ctx=Load()),
                                                                                                        attr='name',
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
                                                                                            targets=[
                                                                                                Subscript(
                                                                                                    value=Name(id='discount', ctx=Load()),
                                                                                                    slice=Constant(value='name', kind=None),
                                                                                                    ctx=Store(),
                                                                                                ),
                                                                                            ],
                                                                                            value=Call(
                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                args=[
                                                                                                    Constant(value='EXTRA CHARGE: %s', kind=None),
                                                                                                    Attribute(
                                                                                                        value=Name(id='invoice_line_form', ctx=Load()),
                                                                                                        attr='name',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                Assign(
                                                                                    targets=[
                                                                                        Subscript(
                                                                                            value=Name(id='discount', ctx=Load()),
                                                                                            slice=Constant(value='amount', kind=None),
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                    ],
                                                                                    value=Name(id='total_discount_amount', ctx=Load()),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[
                                                                                        Subscript(
                                                                                            value=Name(id='discount', ctx=Load()),
                                                                                            slice=Constant(value='tax', kind=None),
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                    ],
                                                                                    value=List(elts=[], ctx=Load()),
                                                                                    type_comment=None,
                                                                                ),
                                                                                For(
                                                                                    target=Name(id='tax', ctx=Store()),
                                                                                    iter=Attribute(
                                                                                        value=Name(id='invoice_line_form', ctx=Load()),
                                                                                        attr='tax_ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    body=[
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Name(id='discount', ctx=Load()),
                                                                                                        slice=Constant(value='tax', kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='append',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='tax', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                    type_comment=None,
                                                                                ),
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='discount_list', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='discount', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='invoice_line_form', ctx=Load()),
                                                                            attr='discount',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=BinOp(
                                                                        left=BinOp(
                                                                            left=Constant(value=1, kind=None),
                                                                            op=Sub(),
                                                                            right=Name(id='total_discount_percentage', ctx=Load()),
                                                                        ),
                                                                        op=Mult(),
                                                                        right=Constant(value=100, kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='discount', ctx=Store()),
                                            iter=Name(id='discount_list', ctx=Load()),
                                            body=[
                                                With(
                                                    items=[
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_form', ctx=Load()),
                                                                        attr='invoice_line_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='new',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            optional_vars=Name(id='invoice_line_form_discount', ctx=Store()),
                                                        ),
                                                    ],
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='invoice_line_form_discount', ctx=Load()),
                                                                        attr='tax_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='clear',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form_discount', ctx=Load()),
                                                                    attr='sequence',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='discount', ctx=Load()),
                                                                slice=Constant(value='seq', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form_discount', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='discount', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='invoice_line_form_discount', ctx=Load()),
                                                                    attr='price_unit',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='discount', ctx=Load()),
                                                                slice=Constant(value='amount', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoice_form', ctx=Load()),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='new_invoice', ctx=Load()),
                                            attr='l10n_it_send_state',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='other', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='body_tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.//Allegati', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='elements', ctx=Load()),
                                    body=[
                                        For(
                                            target=Name(id='element', ctx=Store()),
                                            iter=Name(id='elements', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='name_attachment', ctx=Store())],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='xpath',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='.//NomeAttachment', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='attachment_64', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='str', ctx=Load()),
                                                            attr='encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='element', ctx=Load()),
                                                                            attr='xpath',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.//Attachment', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='attachment_64', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.attachment', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='datas', kind=None),
                                                                    Constant(value='type', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='name_attachment', ctx=Load()),
                                                                    Name(id='attachment_64', ctx=Load()),
                                                                    Constant(value='binary', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='new_invoice', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='no_new_invoice',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='default_res_id',
                                                                        value=Attribute(
                                                                            value=Name(id='new_invoice', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='message_post',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='body',
                                                                value=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Attachment from XML', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='attachment_ids',
                                                                value=List(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='attachment_64', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='message', ctx=Store()),
                                    iter=Name(id='message_to_log', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='new_invoice', ctx=Load()),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Name(id='message', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='invoices', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='new_invoice', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='invoices', ctx=Load()),
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

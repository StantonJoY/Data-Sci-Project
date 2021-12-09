Module(
    body=[
        ImportFrom(
            module='PIL',
            names=[alias(name='Image', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='markupsafe',
            names=[alias(name='Markup', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_qweb_fields',
            names=[alias(name='nl2br', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules',
            names=[alias(name='get_resource_path', asname=None)],
            level=0,
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='sass', asname='libsass')],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='libsass', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Assign(
            targets=[Name(id='DEFAULT_PRIMARY', ctx=Store())],
            value=Constant(value='#000000', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_SECONDARY', ctx=Store())],
            value=Constant(value='#000000', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='BaseDocumentLayout',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Customise the company document layout and display a live preview\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='base.document.layout', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Company Document Layout', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_default_report_footer',
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
                        Assign(
                            targets=[Name(id='footer_fields', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='field', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='field', ctx=Store()),
                                        iter=List(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='phone',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='email',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='website',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='vat',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ifs=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='field', ctx=Load()),
                                                            Name(id='str', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='field', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='Markup', ctx=Load()),
                                        args=[Constant(value=' ', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='footer_fields', ctx=Load())],
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
                    name='_default_company_details',
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
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='address_format', ctx=Store()),
                                        Name(id='company_data', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='_prepare_display_address',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='company_name', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='address_format', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='address_format', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%(company_name)s\n', kind=None),
                                        op=Add(),
                                        right=Name(id='address_format', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='company_data', ctx=Load()),
                                            slice=Constant(value='company_name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='company_data', ctx=Load()),
                                                slice=Constant(value='company_name', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Name(id='Markup', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='nl2br', ctx=Load()),
                                            args=[Name(id='address_format', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Mod(),
                                right=Name(id='company_data', ctx=Load()),
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
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='logo', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.logo', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='preview_logo', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='logo', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Preview logo', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_header', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.report_header', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_footer', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.report_footer', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='_default_report_footer', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_details', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.company_details', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Name(id='_default_company_details', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='paperformat_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.paperformat_id', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='external_report_layout_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.external_report_layout_id', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='font', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.font', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='primary_color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.primary_color', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='secondary_color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.secondary_color', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='custom_colors', ctx=Store())],
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
                                value=Constant(value='_compute_custom_colors', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='logo_primary_color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_logo_colors', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='logo_secondary_color', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_logo_colors', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='layout_background', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.layout_background', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='layout_background_image', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.layout_background_image', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_layout_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='report.layout', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='preview', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_preview', kind=None),
                            ),
                            keyword(
                                arg='sanitize',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.partner_id', kind=None),
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
                    targets=[Name(id='phone', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.phone', kind=None),
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
                    targets=[Name(id='email', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.email', kind=None),
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
                    targets=[Name(id='website', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.website', kind=None),
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
                                arg='related',
                                value=Constant(value='company_id.vat', kind=None),
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
                                arg='related',
                                value=Constant(value='company_id.name', kind=None),
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
                    targets=[Name(id='country_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.country_id', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_custom_colors',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='logo_primary', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='logo_primary_color',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='logo_secondary', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='logo_secondary_color',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='custom_colors',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='logo',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='primary_color',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='secondary_color',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='wizard', ctx=Load()),
                                                                        attr='primary_color',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='lower',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='logo_primary', ctx=Load()),
                                                                        attr='lower',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                        Compare(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='wizard', ctx=Load()),
                                                                        attr='secondary_color',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='lower',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='logo_secondary', ctx=Load()),
                                                                        attr='lower',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                                Constant(value='logo_primary_color', kind=None),
                                Constant(value='logo_secondary_color', kind=None),
                                Constant(value='primary_color', kind=None),
                                Constant(value='secondary_color', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_logo_colors',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='_context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='bin_size', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='wizard_for_image', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='bin_size',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='wizard_for_image', ctx=Store())],
                                            value=Name(id='wizard', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='logo_primary_color',
                                                    ctx=Store(),
                                                ),
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='logo_secondary_color',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='extract_image_primary_secondary_colors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='wizard_for_image', ctx=Load()),
                                                attr='logo',
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='logo', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_preview',
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
                            value=Constant(value=' compute a qweb based preview to display on the wizard ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='styles', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_asset_style',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='wizard', ctx=Load()),
                                        attr='report_layout_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='wizard', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='bin_size', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='wizard_with_logo', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='wizard', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='bin_size',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='wizard_with_logo', ctx=Store())],
                                                    value=Name(id='wizard', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='preview_css', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_css_for_preview',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='styles', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='wizard_with_logo', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='ir_ui_view', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='wizard_with_logo', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='preview',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ir_ui_view', ctx=Load()),
                                                    attr='_render_template',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='web.report_invoice_wizard_preview', kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='company', kind=None),
                                                            Constant(value='preview_css', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='wizard_with_logo', ctx=Load()),
                                                            Name(id='preview_css', ctx=Load()),
                                                        ],
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
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='preview',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
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
                                Constant(value='report_layout_id', kind=None),
                                Constant(value='logo', kind=None),
                                Constant(value='font', kind=None),
                                Constant(value='primary_color', kind=None),
                                Constant(value='secondary_color', kind=None),
                                Constant(value='report_header', kind=None),
                                Constant(value='report_footer', kind=None),
                                Constant(value='layout_background', kind=None),
                                Constant(value='layout_background_image', kind=None),
                                Constant(value='company_details', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_company_id',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='logo',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='logo',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='report_header',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='report_header',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='report_footer',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='wizard', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='report_footer',
                                                    ctx=Load(),
                                                ),
                                                Name(id='str', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='report_footer',
                                            ctx=Load(),
                                        ),
                                        orelse=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='report_footer',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='company_details',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='wizard', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_details',
                                                    ctx=Load(),
                                                ),
                                                Name(id='str', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='company_details',
                                            ctx=Load(),
                                        ),
                                        orelse=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='company_details',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='paperformat_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='paperformat_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='external_report_layout_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='external_report_layout_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='font',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='font',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='primary_color',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='primary_color',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='secondary_color',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='secondary_color',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='wizard_layout', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='report.layout', kind=None),
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
                                                            Constant(value='view_id.key', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='wizard', ctx=Load()),
                                                                        attr='company_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='external_report_layout_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='key',
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
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='report_layout_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='wizard_layout', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='wizard_layout', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[List(elts=[], ctx=Load())],
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
                                        operand=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='primary_color',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='primary_color',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='wizard', ctx=Load()),
                                                        attr='logo_primary_color',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='DEFAULT_PRIMARY', ctx=Load()),
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
                                        operand=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='secondary_color',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='secondary_color',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='wizard', ctx=Load()),
                                                        attr='logo_secondary_color',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='DEFAULT_SECONDARY', ctx=Load()),
                                                ],
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_custom_colors',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='logo',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='custom_colors',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='primary_color',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='wizard', ctx=Load()),
                                                        attr='logo_primary_color',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='DEFAULT_PRIMARY', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='secondary_color',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='wizard', ctx=Load()),
                                                        attr='logo_secondary_color',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='DEFAULT_SECONDARY', ctx=Load()),
                                                ],
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='custom_colors', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_report_layout_id',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='external_report_layout_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='wizard', ctx=Load()),
                                            attr='report_layout_id',
                                            ctx=Load(),
                                        ),
                                        attr='view_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='report_layout_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_logo',
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
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='wizard', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='logo',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='logo',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='primary_color',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='secondary_color',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='wizard', ctx=Load()),
                                        attr='logo_primary_color',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='primary_color',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='logo_primary_color',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='wizard', ctx=Load()),
                                        attr='logo_secondary_color',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='secondary_color',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='logo_secondary_color',
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='logo', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='extract_image_primary_secondary_colors',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='logo', annotation=None, type_comment=None),
                            arg(arg='white_threshold', annotation=None, type_comment=None),
                            arg(arg='mitigate', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=225, kind=None),
                            Constant(value=175, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Identifies dominant colors\n\n        First resizes the original image to improve performance, then discards\n        transparent colors and white-ish colors, then calls the averaging\n        method twice to evaluate both primary and secondary colors.\n\n        :param logo: logo to process\n        :param white_threshold: arbitrary value defining the maximum value a color can reach\n        :param mitigate: arbitrary value defining the maximum value a band can reach\n\n        :return colors: hex values of primary and secondary colors\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='logo', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='logo', ctx=Store()),
                            op=Add(),
                            value=IfExp(
                                test=Compare(
                                    left=Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[Name(id='logo', ctx=Load())],
                                        keywords=[],
                                    ),
                                    ops=[Eq()],
                                    comparators=[Name(id='bytes', ctx=Load())],
                                ),
                                body=Constant(value=b'===', kind=None),
                                orelse=Constant(value='===', kind=None),
                            ),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='image_fix_orientation',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='base64_to_image',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='logo', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='base_w', ctx=Store()),
                                        Name(id='base_h', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='image', ctx=Load()),
                                attr='size',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='w', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Constant(value=50, kind=None),
                                            op=Mult(),
                                            right=Name(id='base_w', ctx=Load()),
                                        ),
                                        op=Div(),
                                        right=Name(id='base_h', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='h', ctx=Store())],
                            value=Constant(value=50, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image_converted', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='image', ctx=Load()),
                                    attr='convert',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='RGBA', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='image_resized', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='image_converted', ctx=Load()),
                                    attr='resize',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Name(id='w', ctx=Load()),
                                            Name(id='h', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='resample',
                                        value=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='NEAREST',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='colors', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='color', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='image_resized', ctx=Load()),
                                    attr='getcolors',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='w', ctx=Load()),
                                        op=Mult(),
                                        right=Name(id='h', ctx=Load()),
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
                                                operand=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='color', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Gt()],
                                                            comparators=[Name(id='white_threshold', ctx=Load())],
                                                        ),
                                                        Compare(
                                                            left=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='color', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Gt()],
                                                            comparators=[Name(id='white_threshold', ctx=Load())],
                                                        ),
                                                        Compare(
                                                            left=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='color', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Gt()],
                                                            comparators=[Name(id='white_threshold', ctx=Load())],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='color', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='colors', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='color', ctx=Load())],
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
                                operand=Name(id='colors', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='primary', ctx=Store()),
                                        Name(id='remaining', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='average_dominant_color',
                                    ctx=Load(),
                                ),
                                args=[Name(id='colors', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='mitigate',
                                        value=Name(id='mitigate', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='secondary', ctx=Store())],
                            value=IfExp(
                                test=Name(id='remaining', ctx=Load()),
                                body=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='average_dominant_color',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='remaining', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='mitigate',
                                                value=Name(id='mitigate', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Name(id='primary', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='l_primary', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='get_lightness',
                                    ctx=Load(),
                                ),
                                args=[Name(id='primary', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='l_secondary', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='get_lightness',
                                    ctx=Load(),
                                ),
                                args=[Name(id='secondary', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='l_primary', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Constant(value=0.2, kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='l_secondary', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Constant(value=0.2, kind=None)],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='l_primary', ctx=Load()),
                                                ops=[GtE()],
                                                comparators=[Constant(value=0.2, kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='l_secondary', ctx=Load()),
                                                ops=[GtE()],
                                                comparators=[Constant(value=0.2, kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='s_primary', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='get_saturation',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='primary', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='s_secondary', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='get_saturation',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='secondary', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='s_primary', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Name(id='s_secondary', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='primary', ctx=Store()),
                                                        Name(id='secondary', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='secondary', ctx=Load()),
                                                    Name(id='primary', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='l_secondary', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Name(id='l_primary', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='primary', ctx=Store()),
                                                        Name(id='secondary', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='secondary', ctx=Load()),
                                                    Name(id='primary', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='rgb_to_hex',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='primary', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='rgb_to_hex',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='secondary', ctx=Load())],
                                        keywords=[],
                                    ),
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
                    name='action_open_base_document_layout',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='action_ref', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='action_ref', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='action_ref', ctx=Store())],
                                    value=Constant(value='web.action_base_document_layout_configurator', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
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
                                args=[Name(id='action_ref', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        slice=Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='res_model', kind=None),
                                            ctx=Load(),
                                        ),
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
                            value=Name(id='res', ctx=Load()),
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
                    name='document_layout_save',
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
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
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
                                        args=[Constant(value='report_action', kind=None)],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[Constant(value='type', kind=None)],
                                        values=[Constant(value='ir.actions.act_window_close', kind=None)],
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
                    name='_get_asset_style',
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
                            value=Constant(value="\n        Compile the style template. It is a qweb template expecting company ids to generate all the code in one batch.\n        We give a useless company_ids arg, but provide the PREVIEW_ID arg that will prepare the template for\n        '_get_css_for_preview' processing later.\n        :return:\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='template_style', ctx=Store())],
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
                                args=[Constant(value='web.styles_company_report', kind=None)],
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='template_style', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=b'', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='company_styles', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='template_style', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='company_ids', kind=None)],
                                        values=[Name(id='self', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='company_styles', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_css_for_preview',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='scss', annotation=None, type_comment=None),
                            arg(arg='new_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Compile the scss into css.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='css_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_scss',
                                    ctx=Load(),
                                ),
                                args=[Name(id='scss', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='css_code', ctx=Load()),
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
                    name='_compile_scss',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='scss_source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        This code will compile valid scss into css.\n        Parameters are the same from odoo/addons/base/models/assetsbundle.py\n        Simply copied and adapted slightly\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='scss_source', ctx=Load()),
                                        attr='strip',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='precision', ctx=Store())],
                            value=Constant(value=8, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='output_style', ctx=Store())],
                            value=Constant(value='expanded', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bootstrap_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_resource_path', ctx=Load()),
                                args=[
                                    Constant(value='web', kind=None),
                                    Constant(value='static', kind=None),
                                    Constant(value='lib', kind=None),
                                    Constant(value='bootstrap', kind=None),
                                    Constant(value='scss', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='libsass', ctx=Load()),
                                            attr='compile',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='string',
                                                value=Name(id='scss_source', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='include_paths',
                                                value=List(
                                                    elts=[Name(id='bootstrap_path', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='output_style',
                                                value=Name(id='output_style', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='precision',
                                                value=Name(id='precision', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='libsass', ctx=Load()),
                                        attr='CompileError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='libsass', ctx=Load()),
                                                    attr='CompileError',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)

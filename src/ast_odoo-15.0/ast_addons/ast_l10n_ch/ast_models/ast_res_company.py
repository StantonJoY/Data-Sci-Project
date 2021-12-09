Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Company',
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
                    value=Constant(value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ch_isr_preprinted_account', ctx=Store())],
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
                                value=Constant(value='Preprinted account', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_ch_isr', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_l10n_ch_isr', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ch_isr_preprinted_bank', ctx=Store())],
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
                                value=Constant(value='Preprinted bank', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_ch_isr', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_l10n_ch_isr', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ch_isr_print_bank_location', ctx=Store())],
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
                                value=Constant(value='Print bank location', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Boolean option field indicating whether or not the alternate layout (the one printing bank name and address) must be used when generating an ISR.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ch_isr_scan_line_left', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Scan line horizontal offset (mm)', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_ch_isr', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_l10n_ch_isr', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ch_isr_scan_line_top', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Scan line vertical offset (mm)', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_ch_isr', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_l10n_ch_isr', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_l10n_ch_isr',
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
                            targets=[Name(id='get_param', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='ir.config_parameter', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='get_param',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='company', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='l10n_ch_isr_preprinted_account',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='get_param', ctx=Load()),
                                                args=[Constant(value='l10n_ch.isr_preprinted_account', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='l10n_ch_isr_preprinted_bank',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='get_param', ctx=Load()),
                                                args=[Constant(value='l10n_ch.isr_preprinted_bank', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='default',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='l10n_ch_isr_scan_line_top',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='get_param', ctx=Load()),
                                                args=[Constant(value='l10n_ch.isr_scan_line_top', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='default',
                                                        value=Constant(value=0, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='l10n_ch_isr_scan_line_left',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='get_param', ctx=Load()),
                                                args=[Constant(value='l10n_ch.isr_scan_line_left', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='default',
                                                        value=Constant(value=0, kind=None),
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
                    name='_set_l10n_ch_isr',
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
                            targets=[Name(id='set_param', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='ir.config_parameter', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='set_param',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='company', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='set_param', ctx=Load()),
                                        args=[
                                            Constant(value='l10n_ch.isr_preprinted_account', kind=None),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='l10n_ch_isr_preprinted_account',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='set_param', ctx=Load()),
                                        args=[
                                            Constant(value='l10n_ch.isr_preprinted_bank', kind=None),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='l10n_ch_isr_preprinted_bank',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='set_param', ctx=Load()),
                                        args=[
                                            Constant(value='l10n_ch.isr_scan_line_top', kind=None),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='l10n_ch_isr_scan_line_top',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='set_param', ctx=Load()),
                                        args=[
                                            Constant(value='l10n_ch.isr_scan_line_left', kind=None),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='l10n_ch_isr_scan_line_left',
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

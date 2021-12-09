Module(
    body=[
        FunctionDef(
            name='migrate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" From 12.0, to saas-13.3, l10n_ch_swissqr_template\n    used to inherit from another template. This isn't the case\n    anymore since https://github.com/odoo/odoo/commit/719f087b1b5be5f1f276a0f87670830d073f6ef4\n    (made in 12.0, and forward-ported). The module will not be updatable if we\n    don't manually clean inherit_id.\n    ", kind=None),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[Constant(value="\n        update ir_ui_view v\n        set inherit_id = NULL, mode='primary'\n        from ir_model_data mdata\n        where\n        v.id = mdata.res_id\n        and mdata.model= 'ir.ui.view'\n        and mdata.name = 'l10n_ch_swissqr_template'\n        and mdata.module='l10n_ch';\n    ", kind=None)],
                        keywords=[],
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

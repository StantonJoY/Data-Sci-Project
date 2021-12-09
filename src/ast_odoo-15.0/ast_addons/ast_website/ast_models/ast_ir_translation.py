Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='IrTranslation',
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
                    value=Constant(value='ir.translation', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_load_module_terms',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='modules', annotation=None, type_comment=None),
                            arg(arg='langs', annotation=None, type_comment=None),
                            arg(arg='overwrite', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add missing website specific translation ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_load_module_terms',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='modules', ctx=Load()),
                                    Name(id='langs', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='overwrite',
                                        value=Name(id='overwrite', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='langs', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='modules', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='overwrite', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='conflict_clause', ctx=Store())],
                                    value=Constant(value="\n                   ON CONFLICT {}\n                   DO UPDATE SET (name, lang, res_id, src, type, value, module, state, comments) =\n                       (EXCLUDED.name, EXCLUDED.lang, EXCLUDED.res_id, EXCLUDED.src, EXCLUDED.type,\n                        EXCLUDED.value, EXCLUDED.module, EXCLUDED.state, EXCLUDED.comments)\n                WHERE EXCLUDED.value IS NOT NULL AND EXCLUDED.value != ''\n            ", kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='conflict_clause', ctx=Store())],
                                    value=Constant(value=' ON CONFLICT DO NOTHING', kind=None),
                                    type_comment=None,
                                ),
                            ],
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
                                    BinOp(
                                        left=Constant(value="\n            INSERT INTO ir_translation(name, lang, res_id, src, type, value, module, state, comments)\n            SELECT DISTINCT ON (specific.id, t.lang, md5(src)) t.name, t.lang, specific.id, t.src, t.type, t.value, t.module, t.state, t.comments\n              FROM ir_translation t\n             INNER JOIN ir_ui_view generic\n                ON t.type = 'model_terms' AND t.name = 'ir.ui.view,arch_db' AND t.res_id = generic.id\n             INNER JOIN ir_ui_view specific\n                ON generic.key = specific.key\n             WHERE t.lang IN %s and t.module IN %s\n               AND generic.website_id IS NULL AND generic.type = 'qweb'\n               AND specific.website_id IS NOT NULL", kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='conflict_clause', ctx=Load()),
                                                attr='format',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='(type, name, lang, res_id, md5(src))', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='langs', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='modules', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='default_menu', ctx=Store())],
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
                                args=[Constant(value='website.main_menu', kind=None)],
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
                                operand=Name(id='default_menu', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
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
                                    BinOp(
                                        left=Constant(value="\n            INSERT INTO ir_translation(name, lang, res_id, src, type, value, module, state, comments)\n            SELECT DISTINCT ON (s_menu.id, t.lang) t.name, t.lang, s_menu.id, t.src, t.type, t.value, t.module, t.state, t.comments\n              FROM ir_translation t\n             INNER JOIN website_menu o_menu\n                ON t.type = 'model' AND t.name = 'website.menu,name' AND t.res_id = o_menu.id\n             INNER JOIN website_menu s_menu\n                ON o_menu.name = s_menu.name AND o_menu.url = s_menu.url\n             INNER JOIN website_menu root_menu\n                ON s_menu.parent_id = root_menu.id AND root_menu.parent_id IS NULL\n             WHERE t.lang IN %s and t.module IN %s\n               AND o_menu.website_id IS NULL AND o_menu.parent_id = %s\n               AND s_menu.website_id IS NOT NULL", kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='conflict_clause', ctx=Load()),
                                                attr='format',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value="(type, lang, name, res_id) WHERE type = 'model'", kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='langs', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='modules', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='default_menu', ctx=Load()),
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
                        Return(
                            value=Name(id='res', ctx=Load()),
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

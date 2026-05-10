package com.example.webapp.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

/**
 * Home Controller - handles home page and basic requests
 */
@Controller
public class HomeController {

    private List<String> messages = new ArrayList<>();

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("title", "Welcome to Java Web App");
        model.addAttribute("currentTime", LocalDateTime.now().format(
                DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
        ));
        model.addAttribute("messages", messages);
        return "index";
    }

    @GetMapping("/about")
    public String about(Model model) {
        model.addAttribute("title", "About This Application");
        model.addAttribute("description", "This is a nice Spring Boot web application built with Maven and generates a WAR file.");
        return "about";
    }

    @PostMapping("/add-message")
    public String addMessage(@RequestParam String message, Model model) {
        if (message != null && !message.trim().isEmpty()) {
            messages.add(message.trim());
        }
        return "redirect:/";
    }

    @GetMapping("/api/health")
    public String health(Model model) {
        model.addAttribute("status", "UP");
        model.addAttribute("timestamp", LocalDateTime.now());
        return "health";
    }
}
